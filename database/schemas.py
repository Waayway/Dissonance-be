from typing import Any, List, Optional

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class ChatroomBase(BaseModel):
    title: str
    description: str
    server_id: Server

class ServerBase(BaseModel):
    title: str
    icon: str

class ServerCreate(ServerBase):
    pass

class Server(ServerBase):
    chatroom_ids: List[chatroom]

class Userbase(BaseModel):
    email: str
    username: str

class UserCreate(Userbase):
    password: str

class User(Userbase):
    id: int
    server_ids: List[Server] = None