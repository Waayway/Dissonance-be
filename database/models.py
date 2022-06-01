from datetime import datetime
import uuid
import peewee
from .database import db

class baseModel(peewee.Model):
    class Meta:
        database = db
    
class User(baseModel):
    id = peewee.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    username = peewee.CharField()
    email = peewee.CharField(unique=True)
    password = peewee.CharField()
    friend_ids = peewee.TextField(null=True)

class Server(baseModel):
    id = peewee.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    title = peewee.CharField()
    icon = peewee.CharField(null=True)
    users = peewee.ManyToManyField(User, backref="servers")

class Chat(baseModel):
    id = peewee.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    title = peewee.CharField()
    description = peewee.CharField()
    server = peewee.ForeignKeyField(Server,backref="chats")
    permission = peewee.CharField(null=True)

class Message(baseModel):
    id = peewee.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    content = peewee.CharField()
    send_time = peewee.DateTimeField(default=datetime.now)
    sender = peewee.ForeignKeyField(User)
    chat = peewee.ForeignKeyField(Chat,backref="messages")


def create_tables():
    with db:
        db.create_tables([User,Server,Chat,Message, Server.users.get_through_model()])
