from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.usecase.note as note_usecase
from api.infrastructure.db import get_db

import api.schemas.note as note_schema

router = APIRouter()


@router.get("/notes", response_model=List[note_schema.Note])
async def list_notes(db: AsyncSession = Depends(get_db)):
    return await note_usecase.get_notes(db)


@router.post("/notes", response_model=note_schema.NoteCreateResponse)
async def create_note(
    note_body: note_schema.NoteCreate, db: AsyncSession = Depends(get_db)
):
    return await note_usecase.create_note(db, note_body)


@router.put("/notes/{note_id}", response_model=note_schema.NoteCreateResponse)
async def update_note(note_id: int, note_body: note_schema.NoteCreate):
    return note_schema.NoteCreateResponse(id=note_id, **note_body.dict())


@router.delete("/notes/{note_id}", response_model=None)
async def delete_note(note_id: int):
    return