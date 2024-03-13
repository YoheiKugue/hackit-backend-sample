from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.infrastructure.db import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    text = Column(String(1024))