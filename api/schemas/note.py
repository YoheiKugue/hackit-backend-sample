from pydantic import BaseModel


class NoteCreate(BaseModel):
    name: str
    text: str


class NoteCreateResponse(NoteCreate):
    id: int

    class Config:
        orm_mode = True


class Note(BaseModel):
    id: int
    name: str
    text: str


class NoteDelete(BaseModel):
    id: int
