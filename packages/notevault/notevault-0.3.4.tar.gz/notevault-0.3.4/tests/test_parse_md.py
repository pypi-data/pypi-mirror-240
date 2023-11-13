from datetime import time, timedelta
from typing import List, Optional, Type

import pytest
from bs4 import BeautifulSoup
from pydantic import BaseModel, ValidationError

from notevault.create_schemas import generate_models_from_yaml
from notevault.environment import ROOT_DIR
from notevault.helper import load_schema
from notevault.parse_md import extract_section_html, parse_section

schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
document_structure = schema["DocumentStructure"]
model_spec = schema["Model"]

with open(f"{ROOT_DIR}/tests/resources/daily_meeting.md", "r") as file:
    md_text = file.read()

# Generate the models
generated_classes = generate_models_from_yaml(model_spec)

GeneralModel = generated_classes["General"]
MeetingModel = generated_classes["Meeting"]


@pytest.mark.parametrize(
    "html_content, model, expected",
    [
        (
            "<ul> <li>start: 07:30</li> <li>end: 18:00</li> <li>breaks: 0:30</li> <li>timestamp: 2020-01-01 07:30</li> <li>date: 2020-01-01</li> </ul>",
            GeneralModel,
            GeneralModel(
                start=time(7, 30),
                end=time(18, 00),
                breaks=timedelta(minutes=30),
                timestamp="2020-01-01 07:30",
                date="2020-01-01",
            ),
        ),
        (
            "<ul> <li>start: 07:30</li> <li>duration: 0:30</li> <li>participants: @user1, @user2</li> </ul>",
            MeetingModel,
            MeetingModel(
                name="meeting",
                start=time(hour=7, minute=30),
                duration=timedelta(minutes=30),
                participants=["@user1", "@user2"],
            ),
        ),
    ],
)
def test_parse_section(html_content: str, model: Type[BaseModel], expected: BaseModel):
    # Parse the html content into a BeautifulSoup object
    section_soup = BeautifulSoup(html_content, "html.parser")

    # Call the parse_section function with the soup and model
    result = parse_section("meeting", section_soup, model)

    # Assert that the result matches the expected model instance
    assert result == expected, f"Expected {expected} but got {result}"


class TestExtractSection:
    import pytest
    from bs4 import BeautifulSoup, NavigableString

    # The fixture for BeautifulSoup object with markdown content
    @pytest.fixture
    def markdown_soup(self):
        markdown_html = """
        <h1>General</h1>
        <p>Some general information here.</p>
        <h1>Meetings</h1>
        <p>Meeting details here.</p>
        <h2>Subsection</h2>
        <p>Subsection content.</p>
        <h1>Another Section</h1>
        <p>Content of another section.</p>
        """
        soup = BeautifulSoup(markdown_html, "html.parser")
        return soup

    # Test if the function correctly extracts a section without subsections
    def test_extract_section_without_subsections(self, markdown_soup):
        section_heading = markdown_soup.find("h1", text="General")
        section_soup = BeautifulSoup(
            extract_section_html(section_heading), "html.parser"
        )
        # Expect only the <p> under "General" to be included
        assert section_soup.find("p").text == "Some general information here."
        assert section_soup.find("h2") is None

    # Test if the function correctly skips other sections
    def test_extract_section_with_subsection_skips_others(self, markdown_soup):
        section_heading = markdown_soup.find("h1", text="Meetings")
        section_soup = BeautifulSoup(
            extract_section_html(section_heading), "html.parser"
        )
        # Expect the <p> and <h2> under "Meetings" to be included, but not "Another Section"
        assert section_soup.find("p").text == "Meeting details here."
        assert section_soup.find("h2").text == "Subsection"
        assert section_soup.find("h1", text="Another Section") is None

    # Test if the function handles the end of document correctly
    def test_extract_section_end_of_document(self, markdown_soup):
        section_heading = markdown_soup.find("h1", text="Another Section")
        section_soup = BeautifulSoup(
            extract_section_html(section_heading), "html.parser"
        )
        # Expect the <p> and <h2> under "Meetings" to be included, but not "Another Section"
        # Expect only the <p> under "Another Section" to be included
        assert section_soup.find("p").text == "Content of another section."
        assert section_soup.find("h1", text="General") is None
