from cgi import test
import unittest 
from database import models, schemas, crud, database

class TestCrudDatabase(unittest.TestCase):
    
    def test_user_crud(self):
        """
        This test creates a user and test different ways to find it
        """
        user_to_create = schemas.UserCreate(**{"email":"example@example.com","username": "testuser", "password": "password"})
        test_user = crud.create_user(user_to_create)
        
        self.assertIsNotNone(test_user)
        self.assertEquals(crud.get_user(test_user.id), test_user)
        self.assertEquals(crud.get_user_by_username(test_user.username), test_user)
        self.assertEquals(crud.get_user_by_email(test_user.email), test_user)

        crud.delete_user(test_user.id)
        
    def test_server_crud(self):
        """
        This test creates a Server and test different ways to find it
        """
        server_to_create = schemas.ServerCreate(**{"title":"testtitle"})
        test_server = crud.create_server(server_to_create)

        self.assertIsNotNone(test_server)
        self.assertEquals(crud.get_server(test_server.id), test_server)
        self.assertEquals(crud.get_server_by_title(test_server.title), test_server)

        crud.delete_server(test_server.id)
    
    def test_chat_crud(self):
        """
        This test creates a chat and tests different ways to find it
        """
        server_for_testing = schemas.ServerCreate(**{"title": "testtitle"})
        test_server = crud.create_server(server_for_testing)
        self.assertIsNotNone(test_server)
        chat_to_create = schemas.ChatroomCreate(**{"title": "Hello, World","description": "Hello, World!", "server": test_server})
        test_chat = crud.create_chat(chat_to_create)
        

        self.assertIsNotNone(test_chat)
        self.assertEquals(crud.get_chat(test_chat.id), test_chat)
        self.assertEquals(crud.get_chat_by_title(test_chat.title), test_chat)

        crud.delete_chat(test_chat.id)
        crud.delete_server(test_server.id)
    

    def test_message_crud(self):
        """
        This test creates a message and required elements and tests different ways to find it
        """
        user_for_testing = schemas.UserCreate(**{"email":"example@example.com","username": "testuser", "password": "password"})
        test_user = crud.create_user(user_for_testing)
        self.assertIsNotNone(test_user)

        server_for_testing = schemas.ServerCreate(**{"title": "testtitle"})
        test_server = crud.create_server(server_for_testing)
        self.assertIsNotNone(test_server)

        chat_for_testing = schemas.ChatroomCreate(**{"title": "Hello, World","description": "Hello, World!", "server": test_server})
        test_chat = crud.create_chat(chat_for_testing)
        self.assertIsNotNone(test_chat)

        message_to_create = schemas.MessageCreate(**{"content": "This is a test message", 'sender': test_user,'chat':test_chat})
        test_message = crud.create_message(message_to_create)

        self.assertIsNotNone(test_message)

        crud.delete_chat(test_chat.id)
        crud.delete_server(test_server.id)
        crud.delete_user(test_user.id)
        crud.delete_message(test_message.id)