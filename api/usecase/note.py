from sqlalchemy.ext.asyncio import AsyncSession

import api.models.note as note_model
import api.schemas.note as note_schema

from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_note(
    db: AsyncSession, note_create: note_schema.NoteCreate
) -> note_model.Note:
    note = note_model.Note(**note_create.dict())
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note


async def get_notes(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                note_model.Note.id,
                note_model.Note.name,
                note_model.Note.text,
            )
        )
    )
    return result.all()


async def get_note(db: AsyncSession, note_id: int) -> Optional[note_model.Note]:
    result: Result = await db.execute(
        select(note_model.Note).filter(note_model.Note.id == note_id)
    )
    note: Optional[Tuple[note_model.Note]] = result.first()
    return note[0] if note is not None else None


async def update_note(
    db: AsyncSession, note_create: note_schema.NoteCreate, original: note_model.Note
) -> note_model.Note:
    original.title = note_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_note(db: AsyncSession, original: note_model.Note) -> None:
    await db.delete(original)
    await db.commit()