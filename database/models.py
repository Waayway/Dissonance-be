from datetime import datetime
import peewee
import uuid
from .database import db

def uuid_gen():
    return str(uuid.uuid4())

class baseModel(peewee.Model):
    class Meta:
        database = db
    
class User(baseModel):
    id = peewee.CharField(unique=True, default=uuid_gen)
    username = peewee.CharField()
    email = peewee.CharField(unique=True)
    password = peewee.CharField()
    friend_ids = peewee.TextField()

class Server(baseModel):
    id = peewee.CharField(unique=True, default=uuid_gen)
    title = peewee.CharField()
    icon = peewee.CharField(null=True)
    users = peewee.ForeignKeyField(User, backref="servers")

class Chat(baseModel):
    id = peewee.CharField(unique=True, default=uuid_gen)
    title = peewee.CharField()
    description = peewee.CharField()
    server_id = peewee.ForeignKeyField(Server,backref="chats")
    permission = peewee.CharField(null=True)

class Message(baseModel):
    id = peewee.CharField(unique=True, default=uuid_gen)
    content = peewee.CharField()
    send_time = peewee.DateTimeField(default=datetime.now)
    sender = peewee.ForeignKeyField(User)
    chat_id = peewee.ForeignKeyField(Chat,backref="messages")


def create_tables():
    with db:
        db.create_tables([User,Server,Chat,Message])
