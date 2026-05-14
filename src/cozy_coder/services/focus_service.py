from datetime import datetime

from cozy_coder.core.database.database import (
    SessionLocal
)

from cozy_coder.core.database.models import (
    FocusSession
)


def save_focus_session(
    tag: str,
    duration: int,
    started_at: datetime,
    ended_at: datetime,
):

    db = SessionLocal()

    session = FocusSession(
        tag=tag,
        duration=duration,
        started_at=started_at,
        ended_at=ended_at,
    )

    db.add(session)

    db.commit()

    db.close()

def get_focus_sessions():

    db = SessionLocal()

    sessions = (
        db.query(FocusSession)
        .order_by(FocusSession.created_at.desc())
        .all()
    )

    db.close()

    return sessions

def delete_focus_session(session_id: int):

    db = SessionLocal()

    session = (
        db.query(FocusSession)
        .filter(FocusSession.id == session_id)
        .first()
    )

    if session:

        db.delete(session)

        db.commit()

    db.close()