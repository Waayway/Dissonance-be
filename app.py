from fastapi import FastAPI
from fastapi import responses
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import users
from database import get_db, create_tables

db = get_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ToDocs():
    return responses.RedirectResponse('/docs')


app.include_router(users.router)

if __name__ == "__main__":
    create_tables()
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    
