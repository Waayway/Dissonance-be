from . import database, models
from .database import db_state_default
from fastapi import Depends

def create_tables():
    models.create_tables()

async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()

def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()
    return database.db