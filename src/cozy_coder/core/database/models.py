from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from datetime import datetime

from cozy_coder.core.database.database import Base


class FocusSession(Base):

    __tablename__ = "focus_sessions"

    id = Column(Integer, primary_key=True)

    tag = Column(String)

    started_at = Column(DateTime)

    ended_at = Column(DateTime)

    duration = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )