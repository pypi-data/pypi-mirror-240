from datetime import time, datetime, timedelta, date
from typing import List, Dict, Type, Any, Optional

import dateutil.parser
from pydantic import BaseModel, ValidationError
from bs4 import BeautifulSoup, Tag
from markdown import markdown

# Assume that `generated_schemas` is a dictionary with keys as class names and values as Pydantic classes.
generated_classes: Dict[str, Type[BaseModel]] = {}


def parse_time_element(text: str) -> time:
    time_str = text.split(" ", maxsplit=1)[-1].strip()
    parsed_time = datetime.strptime(time_str, "%H:%M").time()
    return parsed_time


def parse_timedelta_element(text: str) -> timedelta:
    # Extract the time duration part after the prefix 'bla: '
    time_part = text.split(" ")[-1].strip()  # This gets the '0:30' part
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
    """Extracts data from the section BeautifulSoup object and creates an instance of the specified Pydantic model."""
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
                else field_content.parent
            )
            if not value_tag:
                continue
            if value_tag.name.startswith("h"):
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
