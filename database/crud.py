import os
from passlib.hash import bcrypt_sha256
from . import models, schemas
from .models import *

SECRET_KEY = os.getenv("SECRET_KEY")

##
## Get User by x
##

def get_user(user_id: str):
    return schemas.User.from_orm(User.select().where(User.id == user_id).get())

def get_user_by_username(username: str):
    return schemas.User.from_orm(User.select().where(User.username == username))

def get_user_by_email(email: str):
    return schemas.User.from_orm(User.select().where(User.email == email).get())

def get_user_by_name_with_password(name: str):
    user = User.select().where(User.username == name).get()
    if user is None:
        return user
    return schemas.UserCreate.from_orm(user)

##
## Create User
## 
def create_user(user: schemas.UserCreate):
    password = bcrypt_sha256(str(user.password)+SECRET_KEY)
    db_user = User.create(username=user.username, email=user.email, password=password)
    return schemas.User.from_orm(db_user)

##
## Get server by x
##
def get_server(server_id: str):
    return schemas.Server.from_orm(Server.select().where(Server.id == server_id).get())

def get_server_by_title(server_title: str):
    return schemas.Server.from_orm(Server.select().where(Server.title == server_title).get())

##
## Create/delete Server
##

def create_server(server: schemas.ServerCreate):
    db_server = Server.create(title=server.title)
    return schemas.Server.from_orm(db_server)

def delete_server(server_id: str):
    Server.delete().where(Server.id == server_id).execute()

##
## get Chat by x
##
def get_chat(chat_id: str):
    return schemas.Chatroom.from_orm(Chat.select().where(Chat.id == chat_id).get())

def get_chat_by_title(chat_title: str):
    return schemas.Chatroom.from_orm(Chat.select().where(Chat.title == chat_title).get())

##
## creating and deleting chats
##
def create_chat(chat: schemas.ChatroomCreate):
    chat_db = Chat.create(title=chat.title, description=chat.description, server_id=chat.server_id)
    return schemas.Chatroom.from_orm(chat_db)

def delete_chat(chat_id: str):
    Chat.delete().where(Chat.id == chat_id).execute()

##
## get Messages by x
##
def get_message(message_id: str):
    return schemas.Message.from_orm(Message.select().where(Message.id == message_id))

def get_messages_by_chat(chat_id: str):
    return Message.select().where(Message.chat_id == chat_id)

##
## Create and delete message
##
def create_message(message: schemas.MessageCreate):
    Message.create(content=message.content, sender=message.sender_id, chat_id=message.chat_id)