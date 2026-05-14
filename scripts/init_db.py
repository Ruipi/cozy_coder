from cozy_coder.core.database.database import (
    engine,
    Base
)

from cozy_coder.core.database.models import FocusSession


Base.metadata.create_all(bind=engine)

print("Database initialized.")