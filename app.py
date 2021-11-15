from fastapi import FastAPI
from fastapi import responses, Depends
import uvicorn

import users
from database import crud, database, models, schemas
from database.database import db_state_default

database.db.connect()
database.db.create_tables([models.Chatroom,models.User,models.Server,models.Message])
database.db.close()

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





app = FastAPI()

@app.get("/")
def ToDocs():
    return responses.RedirectResponse('/docs')


app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
