from peewee import ForeignKeyField, Model, ModelBase, CharField, ManyToManyField
from peewee import SqliteDatabase

db = SqliteDatabase("sqlite.db")

class User(Model):
    username = CharField()
    password = CharField()
    
    class Meta:
        database = db
    
    def get_servers(self):
        return (User.get(User == self).servers.order_by(Server.id))
    

class Server(Model):
    name = CharField()
    description = CharField()
    people = ManyToManyField(User, backref="servers")

    class Meta:
        database = db
    
    def get_chatrooms(self):
        return (Chatroom.select().join(Server).where(Server == self))

Server.people.get_through_model()

class Chatroom(Model):
    name = CharField()
    description = CharField
    Server = ForeignKeyField(Server, backref="chats")

    class Meta:
        database = db
        
def create_tables():
    with db:
        db.create_tables([User,Server,Chatroom])