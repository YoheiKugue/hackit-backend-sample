from pydantic import BaseModel


class NoteCreate(BaseModel):
    name: str
    text: str


class Note(BaseModel):
    id: int
    name: str
    text: str


class NoteDelete(BaseModel):
    id: int
