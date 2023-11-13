from typing import TypeVar

from bs4 import Tag
from pydantic import BaseModel

# T = TypeVar('T', bound=BaseModel)


class Section:
    def __init__(self, heading: str, content: list[Tag] = None):
        self.heading = heading
        self.content = content
