import sys
import unittest

from src import models
from src.app import create_app
from src.database import db


class TestAuthentication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()[1]
        cls.test_user = {
            'username': 'test_user',
            'password': 'my_password_123',
            'first_name': 'Jim',
            'last_name': 'Johnson'
        }

        if not cls.app.config["TESTING"]:
            sys.exit("Testing mode is not enabled. Ensure that the testing configuration is used")

        cls.test_client = cls.app.test_client()

        with cls.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

            user = models.User(**cls.test_user)
            db.session.add(user)
            db.session.commit()

    def test_access_denied(self):
        r = self.test_client.get("/auth/echo/message")
        self.assertEqual(r.status_code, 401)

    def test_login_logout(self):
        r = self.test_client.post("/auth/login", data=self.test_user)
        self.assertEqual(r.status_code, 200)

        r = self.test_client.get("/auth/echo/message")
        self.assertEqual(r.status_code, 200)

        r = self.test_client.post("/auth/logout")
        self.assertEqual(r.status_code, 200)

        r = self.test_client.get("/auth/echo/message")
        self.assertEqual(r.status_code, 401)

    def test_login_invalid_username(self):
        r = self.test_client.post('/auth/login', data={
            'username': 'jim',
            'password': self.test_user['password']
        })
        self.assertEqual(r.status_code, 401)

        r = self.test_client.get('/auth/echo/message')
        self.assertEqual(r.status_code, 401)

    def test_login_invalid_password(self):
        r = self.test_client.post('/auth/login', data={
            'username': self.test_user['username'],
            'password': 'some_password'
        })
        self.assertEqual(r.status_code, 401)

        r = self.test_client.get('/auth/echo/message')
        self.assertEqual(r.status_code, 401)
