import pytest
from pydantic import BaseModel, ValidationError
from bs4 import BeautifulSoup

from notevault.parse_md import parse_markdown


# Assuming extract_section and parse_section are defined as before
# Assuming markdown function converts markdown to HTML


# A mock Pydantic model for testing
class MockModel(BaseModel):
    name: str
    detail: str


@pytest.fixture
def mock_generated_classes():
    return {"MockModel": MockModel}


@pytest.fixture
def mock_document_structure():
    return {
        "Sections": [
            {"section": {"heading": "# General", "type": "MockModel", "is_list": False}}
        ]
    }


@pytest.fixture
def markdown_text():
    return """
# General
Detail of general section

# Another Section
This section should not be parsed
"""


# Test parsing a simple markdown with one section
def test_parse_markdown_single_section(
    markdown_text, mock_document_structure, mock_generated_classes
):
    parsed_models = parse_markdown(
        markdown_text, mock_document_structure, mock_generated_classes
    )
    assert len(parsed_models) == 1
    assert parsed_models[0].name == "General"
    assert parsed_models[0].detail == "Detail of general section"


# Test parsing a markdown with a list of sections
@pytest.fixture
def markdown_text_with_list():
    return """
# Meetings
## Meeting 1
Detail of meeting 1

## Meeting 2
Detail of meeting 2
"""


@pytest.fixture
def mock_document_structure_with_list():
    return {
        "Sections": [
            {"section": {"heading": "# Meetings", "type": "MockModel", "is_list": True}}
        ]
    }


def test_parse_markdown_section_list(
    markdown_text_with_list, mock_document_structure_with_list, mock_generated_classes
):
    parsed_models = parse_markdown(
        markdown_text_with_list,
        mock_document_structure_with_list,
        mock_generated_classes,
    )
    assert len(parsed_models) == 2
    assert parsed_models[0].name == "Meeting 1"
    assert parsed_models[0].detail == "Detail of meeting 1"
    assert parsed_models[1].name == "Meeting 2"
    assert parsed_models[1].detail == "Detail of meeting 2"
