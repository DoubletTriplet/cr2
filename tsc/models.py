from pydantic import BaseModel
from typing import List


class Word(BaseModel):
    word: str
    definitions: List|None = []
    synonyms: List|None = []
    translations: List|None = []
    examples: List|None = []
