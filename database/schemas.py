from typing import Any, ForwardRef, List, Optional
from datetime import date
from uuid import UUID
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class baseModel(BaseModel):
    class Config:
        orm_mode=True
        getter_dict=PeeweeGetterDict


#
# Message
#
chat = ForwardRef('ChatroomWithoutMessages')
user = ForwardRef('User')
class MessageBase(baseModel):
    content: str
    sender: user
    chat: chat

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: UUID
    send_time: date

#
# Chatroom
#
server = ForwardRef('ServerWithoutChats')
class ChatroomBase(baseModel):
    title: str
    description: str
    server: server
    

class ChatroomCreate(ChatroomBase):
    pass
class ChatroomWithoutMessages(ChatroomBase):
    id: UUID
    permission: str = None

class Chatroom(ChatroomBase):
    id: UUID
    messages: list[Message]
    permission: str = None
#
# Server
#
class ServerBase(baseModel):
    title: str

class ServerCreate(ServerBase):
    pass

class ServerWithoutChats(ServerBase):
    id: UUID
    icon: str = None
    users: List[str] = None

class Server(ServerBase):
    id: UUID
    icon: str = None
    chats: List[Chatroom] = None
    users: List[str] = None




#
# User
#
class Userbase(baseModel):
    email: str
    username: str

class UserCreate(Userbase):
    password: str

class User(Userbase):
    id: UUID
    servers: List[ServerWithoutChats] = None


update_forward_ref_list = [
    Chatroom,
    ChatroomBase,
    ChatroomCreate,
    ChatroomWithoutMessages,
    Message,
    MessageBase,
    MessageCreate
]
for i in update_forward_ref_list:
    i.update_forward_refs()



