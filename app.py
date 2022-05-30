from fastapi import FastAPI
from fastapi import responses
import uvicorn

import users
from database import get_db, create_tables

create_tables()
db = get_db()

app = FastAPI()

@app.get("/")
def ToDocs():
    return responses.RedirectResponse('/docs')


app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
