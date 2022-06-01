import os
from passlib.hash import bcrypt
from . import models, schemas
from .models import *

SECRET_KEY = os.getenv("SECRET_KEY")

##
## Get User by x
##

def get_user(user_id: str):
    return schemas.User.from_orm(User.select().where(User.id == user_id).get())

def get_user_by_username(username: str):
    return schemas.User.from_orm(User.select().where(User.username == username).get())

def get_user_by_email(email: str):
    return schemas.User.from_orm(User.select().where(User.email == email).get())

def get_user_by_name_with_password(name: str):
    user = User.select().where(User.username == name).get()
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
    server_db = Server.select().where(Server.id == chat.server.id).get()
    chat_db = Chat.create(title=chat.title, description=chat.description, server=server_db)
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
    sender = User.select().where(User.id == message.sender.id).get()
    chat = Chat.select().where(Chat.id == message.chat.id).get()
    message_db = Message.create(content=message.content, sender=sender, chat=chat)
    return schemas.Message.from_orm(message_db)

def delete_message(message_id: str):
    Message.delete().where(Message.id == message_id).execute()