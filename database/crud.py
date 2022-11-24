import os
from passlib.hash import bcrypt
from . import models, schemas
from .models import *

SECRET_KEY = os.getenv("SECRET_KEY")

##
## Get User by x
##

def get_user(user_id: str):
    user = User.filter(User.id == user_id).first()
    if not user:
        return None    
    return schemas.User.from_orm(user)

def get_user_by_username(username: str):
    user = User.filter(User.username == username).first()
    if not user:
        return None
    return schemas.User.from_orm(user)

def get_user_by_email(email: str):
    user = User.filter(User.email == email).first()
    if not user:
        return None
    return schemas.User.from_orm(user)

def get_user_by_name_with_password(name: str):
    user = User.filter(User.username == name).first()
    if user is None:
        return user
    return schemas.UserCreate.from_orm(user)

##
## Create and Delete User
## 
def create_user(user: schemas.UserCreate):
    password = bcrypt.hash(str(user.password)+SECRET_KEY)
    db_user = User.create(username=user.username, email=user.email, password=password)
    return schemas.User.from_orm(db_user)

def delete_user(user_id: str):
    User.delete().where(User.id == user_id).execute()
##
## Authentication
##
def authenticate_user(username: str, password: str):
    user = get_user_by_name_with_password(username)
    if not user:
        return False
    if not bcrypt.verify(str(password)+SECRET_KEY,user.password):
        return False
    return get_user_by_username(username)

##
## Modifying UserData
##



##
## Get server by x
##
def get_server(server_id: str):
    server = Server.filter(Server.id == server_id).first()
    if not server:
        return None
    return schemas.Server.from_orm(server)

def get_server_by_title(server_title: str):
    server = Server.filter(Server.title == server_title).first()
    if not server:
        return None
    return schemas.Server.from_orm(server)

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
    chat = Chat.filter(Chat.id == chat_id).first()
    if not chat:
        return None
    return schemas.Chatroom.from_orm(chat)

def get_chat_by_title(chat_title: str):
    chat = Chat.filter(Chat.title == chat_title).first()
    if not chat:
        return None
    return schemas.Chatroom.from_orm(chat)

##
## creating and deleting chats
##
def create_chat(chat: schemas.ChatroomCreate):
    server_db = Server.select().where(Server.id == chat.server.id).get()
    chat_db = Chat.create(title=chat.title, description=chat.description, server=server_db)
    return schemas.Chatroom.from_orm(chat_db)

def delete_chat(chat_id: str):
    Chat.delete().where(Chat.id == chat_id).execute()

##
## get Messages by x
##
def get_message(message_id: str):
    message = Message.filter(Message.id == message_id)
    if not message:
        return None
    return schemas.Message.from_orm(message)

def get_messages_by_chat(chat_id: str):
    return Message.select().where(Message.chat_id == chat_id)

##
## Create and delete message
##
def create_message(message: schemas.MessageCreate):
    sender = User.select().where(User.id == message.sender.id).get()
    chat = Chat.select().where(Chat.id == message.chat.id).get()
    message_db = Message.create(content=message.content, sender=sender, chat=chat)
    return schemas.Message.from_orm(message_db)

def delete_message(message_id: str):
    Message.delete().where(Message.id == message_id).execute()