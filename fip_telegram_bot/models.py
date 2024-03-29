from typing import List, Optional, Dict

from pydantic import BaseModel


class Track(BaseModel):
    title: str
    album: Optional[str]
    artist: str
    year: Optional[int]
    label: Optional[str]
    musical_kind: Optional[str]
    external_urls: Dict[str, str] = {}


class Radio(BaseModel):
    name: str
    url: str
