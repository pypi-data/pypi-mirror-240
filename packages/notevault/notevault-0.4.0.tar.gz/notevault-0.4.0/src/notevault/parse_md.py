import re
from datetime import date, datetime, time, timedelta
from typing import Any, Dict, List, Optional, Type, Union, get_args, get_origin

import dateutil.parser
import yaml
from bs4 import BeautifulSoup, Tag
from markdown import markdown
from pydantic import BaseModel, ValidationError

from notevault.helper import string_to_yaml

# Assume that `generated_schemas` is a dictionary with keys as class names and values as Pydantic classes.
generated_classes: Dict[str, Type[BaseModel]] = {}


def parse_int_element(text: str) -> int:
    # Extracts the integer part after the prefix (e.g., 'duration: 30')
    int_part = text.split(" ")[-1].strip()
    if not re.match(r"^\d+$", int_part):
        raise ValueError(f"Invalid integer format: [{int_part}]")
    return int(int_part)


def parse_time_element(text: str) -> time:
    time_str = text.split(" ", maxsplit=1)[-1].strip()
    if not re.match(r"^\d{1,2}:\d{2}$", time_str):
        raise ValueError(f"Invalid time format: [{time_str}]")
    parsed_time = datetime.strptime(time_str, "%H:%M").time()
    return parsed_time


def parse_timedelta_element(text: str) -> timedelta:
    # Extract the time duration part after the prefix 'bla: '
    time_part = text.split(" ")[-1].strip()  # This gets the '0:30' part
    if not re.match(r"^\d{1,2}:\d{2}$", time_part):
        raise ValueError(f"Invalid time duration format: [{time_part}]")
    hours, minutes = map(int, time_part.split(":"))
    return timedelta(hours=hours, minutes=minutes)


def parse_datetime_element(text: str) -> datetime:
    # Strips the leading 'timestamp:' if present and any surrounding whitespace
    clean_text = text.split(":", 1)[-1].strip()
    return dateutil.parser.parse(clean_text)


def parse_date_element(text: str) -> date:
    # Strips the leading label if present and any surrounding whitespace
    clean_text = text.split(":", 1)[-1].strip()
    return dateutil.parser.parse(clean_text).date()


def parse_section(
    name: str, section_soup: BeautifulSoup, model: Type[BaseModel]
) -> BaseModel:
    """Extracts data from the section BeautifulSoup object
    and creates an instance of the specified Pydantic model.
    """
    data: Dict[str, Any] = {}
    if "name" in model.model_fields:
        data["name"] = name

    # Iterate through the model's fields and extract data from the soup
    for field_name, field_info in model.model_fields.items():
        # syntax: 'text and field_name in text'
        # ensure that the text is not None or empty before checking if it contains field_name.
        # safeguard to ensure that the lambda only returns True when there's actual non-empty text that includes the field_name
        # lambda: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id11
        field_content = section_soup.find(
            string=lambda text: text and field_name in text.lower()
        )

        if field_content:
            # Get the sibling or parent tag that contains the actual field data
            value_tag = (
                field_content.find_next_sibling()
                if isinstance(field_content, Tag)
                else field_content.parent  # gets enclosing tag
            )
            if not value_tag:
                continue
            if value_tag.name.startswith("h"):  # go one level deeper
                # If the value tag is a heading, extract the HTML of the section
                value_tag = BeautifulSoup(
                    extract_section_html(value_tag), "html.parser"
                )

            if field_info.annotation in [time, Optional[time]]:
                data[field_name] = parse_time_element(value_tag.text)
            elif field_info.annotation in [timedelta, Optional[timedelta]]:
                data[field_name] = parse_timedelta_element(value_tag.text)
            elif field_info.annotation in [datetime, Optional[datetime]]:
                data[field_name] = parse_datetime_element(value_tag.text)
            elif field_info.annotation in [date, Optional[date]]:
                data[field_name] = parse_date_element(value_tag.text)
            elif field_info.annotation in [List[str], Optional[List[str]]]:
                data[field_name] = value_tag.text.strip()
                list_str = value_tag.text.split(":", maxsplit=1)[-1].strip()
                data[field_name] = [item.strip() for item in list_str.split(",")]
            elif field_info.annotation in [int, Optional[int]]:
                data[field_name] = parse_int_element(value_tag.text)
            else:
                data[field_name] = value_tag.text.strip()

    return model(**data)


def parse_markdown(
    md_text: str,
    document_structure: Dict,
    generated_classes: Dict[str, Type[BaseModel]],
) -> List[BaseModel]:
    soup = BeautifulSoup(markdown(md_text), "html.parser")
    parsed_models = []

    for section_info in document_structure.get("Sections"):
        heading = section_info["section"]["heading"]
        class_name = section_info["section"]["type"]
        is_list = section_info["section"]["is_list"]

        # Find the heading in the markdown
        heading_level = f"h{heading.count('#')}"
        section_heading = soup.find(heading_level, string=heading.strip("# ").strip())

        if section_heading is None:
            continue

        section_soup = BeautifulSoup(
            extract_section_html(section_heading), "html.parser"
        )

        model_class = generated_classes.get(class_name)
        if not model_class:
            continue

        try:
            if is_list:
                # 1. Flat list: <ul> with <li> children
                if is_only_ul_with_no_subheadings(section_soup):
                    p = ListSoupParser(section_soup, model_class)
                    parsed_models.extend(p.parse_ul_to_models())
                # 2. Subheadings
                else:
                    # Process each list item within the section
                    sub_heading_level = f"h{heading.count('#') + 1}"
                    list_items = section_soup.find_all(sub_heading_level)
                    for list_item in list_items:
                        section_soup = BeautifulSoup(
                            extract_section_html(list_item), "html.parser"
                        )
                        model_instance = parse_section(
                            list_item.get_text(strip=True), section_soup, model_class
                        )
                        parsed_models.append(model_instance)
            else:
                # Process the whole section once
                model_instance = parse_section(
                    section_heading.text, section_soup, model_class
                )
                parsed_models.append(model_instance)
        except ValidationError as e:
            new_exception = RuntimeError(
                f"Data validation error for section {class_name}"
            )
            raise new_exception from e

    return parsed_models


def extract_section_html(value_tag: Tag) -> str:
    """
    Extracts the HTML of a section starting with value_tag (a heading) and
    includes all subsequent tags until the next heading of same or higher level.

    Tag Object: represents an HTML or XML tag in the original document.
    For example, in an HTML document, <p>, <div>, <a>, and <li> are all tags that can be represented
    as Tag objects in BeautifulSoup.

    Value Tag: Tag object that contains the specific piece of data you're
    trying to extract. For example, if you're parsing an HTML page to extract the text of a paragraph,
    the Tag object representing the <p> tag with that text would be the "value tag."

    Extracting Data: To extract data from a "value tag," you would typically access its .text attribute
    or use methods like .get_text(). These methods aggregate the text of a tag and all its descendants,
    returning it as a single string.
    """
    heading_level = int(value_tag.name[1:])  # Converts 'h2' to 2, 'h3' to 3, etc.

    # Accumulate elements until the next heading of the same or higher level
    section_content = []
    for sibling in value_tag.next_siblings:
        # If sibling is a Tag and a heading of the same or higher level, break the loop
        if (
            isinstance(sibling, Tag)
            and sibling.name.startswith("h")
            and int(sibling.name[1:]) <= heading_level
        ):
            break
        section_content.append(str(sibling))
    # Join all elements to form the HTML of the section
    section_html = "".join(section_content)
    return section_html


def is_only_ul_with_no_subheadings(section_soup: BeautifulSoup) -> bool:
    # Check if section_soup has only one child and it's a <ul> tag
    children = [child for child in section_soup.children if isinstance(child, Tag)]
    if len(children) != 1 or children[0].name != "ul":
        return False

    # Check inside the <ul> tag for subheadings or other tags
    ul_tag = children[0]
    for item in ul_tag.descendants:
        if isinstance(item, Tag) and item.name.startswith("h"):
            return False  # Found a subheading tag
        if isinstance(item, Tag) and item.name != "li":
            return False  # Found a tag other than <li> within <ul>

    return True


class ListSoupParser:
    """Parses a BeautifulSoup object that contains a list of items into a list of Pydantic models."""

    def __init__(self, list_soup: BeautifulSoup, schema: Type[BaseModel]) -> None:
        assert is_only_ul_with_no_subheadings(
            list_soup
        ), f"Expected only <ul> tag with <li> children in this section, but got {list_soup}"
        self.soup = list_soup
        self.schema = schema

    @staticmethod
    def parse_string_to_type(value: str, field_type: type) -> any:
        if not value:
            return None

        # Handle Optional types
        if get_origin(field_type) is Union:
            field_type = next(t for t in get_args(field_type) if t is not type(None))

        if issubclass(field_type, time):
            return datetime.strptime(value, "%H:%M").time()
        elif issubclass(field_type, timedelta):
            hours, minutes = map(int, value.split(":"))
            return timedelta(hours=hours, minutes=minutes)
        elif issubclass(field_type, int):
            return int(value)
        else:
            return value

    def parse_li_to_model(self, li_tag) -> BaseModel:
        text = li_tag.get_text()
        yaml_text = string_to_yaml(text)
        try:
            data = yaml.safe_load(yaml_text)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            raise
        field_values = {}
        for field_name, field_value in data.items():
            field_type = self.schema.__annotations__.get(field_name)
            if field_type:
                field_values[field_name] = self.parse_string_to_type(
                    field_value, field_type
                )

        return self.schema(**field_values)

    def parse_ul_to_models(self) -> List[BaseModel]:
        models = []
        for li_tag in self.soup.find_all("li"):
            model = self.parse_li_to_model(li_tag)
            models.append(model)
        return models
