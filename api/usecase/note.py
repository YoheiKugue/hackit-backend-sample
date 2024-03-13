from sqlalchemy.ext.asyncio import AsyncSession

import api.models.note as note_model
import api.schemas.note as note_schema

from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_note(
    db: AsyncSession, note_create: note_schema.noteCreate
) -> note_model.note:
    note = note_model.note(**note_create.dict())
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note


async def get_notes_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                note_model.note.id,
                note_model.note.title,
                note_model.Done.id.isnot(None).label("done"),
            ).outerjoin(note_model.Done)
        )
    )
    return result.all()


async def get_note(db: AsyncSession, note_id: int) -> Optional[note_model.note]:
    result: Result = await db.execute(
        select(note_model.note).filter(note_model.note.id == note_id)
    )
    note: Optional[Tuple[note_model.note]] = result.first()
    return note[0] if note is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def update_note(
    db: AsyncSession, note_create: note_schema.noteCreate, original: note_model.note
) -> note_model.note:
    original.title = note_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_note(db: AsyncSession, original: note_model.note) -> None:
    await db.delete(original)
    await db.commit()