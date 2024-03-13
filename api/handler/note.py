from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.usecase.note as note_crud
from api.infrastructure.db import get_db

import api.schemas.note as note_schema

router = APIRouter()


@router.get("/notes", response_model=List[note_schema.Note])
async def list_notes():
    return [note_schema.Note(id=1, name="sample note", text="sample text")]


@router.post("/notes", response_model=note_schema.noteCreateResponse)
async def create_note(
    note_body: note_schema.noteCreate, db: AsyncSession = Depends(get_db)
):
    return await note_crud.create_note(db, note_body)


@router.put("/notes/{note_id}", response_model=note_schema.noteCreateResponse)
async def update_note(note_id: int, note_body: note_schema.noteCreate):
    return note_schema.noteCreateResponse(id=note_id, **note_body.dict())


@router.delete("/notes/{note_id}", response_model=None)
async def delete_note(note_id: int):
    return