from typing import List, Optional, Dict

from pydantic import BaseModel


class Song(BaseModel):
    title: str
    album: str
    artist: str
    year: Optional[int]
    label: Optional[str]
    musical_kind: Optional[str]
    external_urls: Dict[str, str] = {}


class Image(BaseModel):
    height: int
    url: str
    width: int


class Album(BaseModel):
    id: str
    images: List[Image]
    href: str
    name: str
    release_date: str
    uri: str


class Artist(BaseModel):
    id: str
    href: str
    name: str
    uri: str


class Track(BaseModel):
    album: Album
    artists: List[Artist]
    duration_ms: int
    id: str
    preview_url: Optional[str]
    uri: str
    name: str


class Station(BaseModel):
    name: str
