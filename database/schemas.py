from typing import Any, List, Optional
from datetime import date
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

#
# Message
#
class MessageBase(BaseModel):
    content: str
    sender_id: str
    chat_id: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    send_time: date

#
# Chatroom
#
class ChatroomBase(BaseModel):
    title: str
    description: str
    server_id: str
    permission: str = None

class ChatroomCreate(ChatroomBase):
    pass

class Chatroom(ChatroomBase):
    pass

#
# Server
#
class ServerBase(BaseModel):
    title: str

class ServerCreate(ServerBase):
    pass

class Server(ServerBase):
    icon: str = None
    chats: List[Chatroom] = None
    users: List[str] = None


#
# User
#
class Userbase(BaseModel):
    email: str
    username: str

class UserCreate(Userbase):
    password: str

class User(Userbase):
    id: int
    servers: List[Server] = None



