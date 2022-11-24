from operator import ge
from fastapi import APIRouter, Depends
from database import schemas, crud
from users import get_current_user

import json

router = APIRouter(prefix="/friends/")

@router.get("/")
async def get_friends(user: schemas.User = Depends(get_current_user)):
    friends = json.loads(user.friend_ids);
    return friends

@router.post("/add")
async def add_friends(friend: schemas.addFriendData, user: schemas.User = Depends(get_current_user)):
    friend_id = friend.friend.id