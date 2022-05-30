from fastapi import APIRouter
import fastapi_bearer_auth as fba

router = APIRouter()

@fba.handle_get_user_by_name
async def get_user_by_name(name):
    return 'no'

@fba.handle_create_user
async def create_user(username,password):
    user = {
        "username": username,
        "password": await fba.call_config('get_password_hash', password),
    }

    return user

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}