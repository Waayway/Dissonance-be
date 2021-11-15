import peewee
from .database import db

class baseModel(peewee.ModelBase):
    class Meta:
        database = db

class User(baseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField(unique=True)
    server_ids = peewee.ManyToManyField()

class Server(baseModel):
    title = peewee.CharField()
    icon = peewee.CharField()
    chatroom_ids = peewee.ManyToManyField()

class Chatroom(baseModel):
    title = peewee.CharField()
    description = peewee.CharField()
    Server_id = peewee.ForeignKeyField()
    message_ids = peewee.ManyToManyField()

class Message(baseModel):
    content = peewee.CharField()
    date_time = peewee.DateTimeField()
    sender_id = peewee.ForeignKeyField()
    chatroom_id = peewee.ForeignKeyField()

User.server_ids.model = Server
Server.chatroom_ids.model = Chatroom
Chatroom.message_ids.model = Message
Chatroom.Server_id.model = Server
Message.sender_id.model = User
Message.chatroom_id.model = Chatroom

