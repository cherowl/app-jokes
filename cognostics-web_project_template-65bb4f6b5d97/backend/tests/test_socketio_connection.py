import sys
import unittest
from time import sleep

import requests
from socketIO_client import SocketIO
from socketIO_client.exceptions import ConnectionError

from src import models
from src.app import create_minimal_app
from src.database import db
from tests.utils import ServerProcess


class StopWaitingException(Exception):
    pass


class TestSocketIOConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_user = {
            'username': 'test_user',
            'password': 'my_password123',
            'first_name': 'Jim',
            'last_name': 'Johnson'
        }
        cls.app = create_minimal_app()
        cls.APP_PORT = cls.app.config["APP_PORT"]
        cls.server_process = ServerProcess()
        # wait a bit for the server to wake up
        sleep(5)

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

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

    def send_message(self, outgoing_event, incoming_event, data):
        received_data = None

        def on_response(*args):
            nonlocal received_data
            received_data, = args
            # raising this exception will break out of the wait loop
            raise StopWaitingException

        r = requests.post("http://localhost:{}/auth/login".format(self.APP_PORT), data=self.test_user)
        self.assertEqual(r.status_code, 200)

        with SocketIO('localhost', self.APP_PORT, cookies={'session': r.cookies['session']},
                      wait_for_connection=True) as socketIO:
            socketIO.emit(outgoing_event, data)
            socketIO.on(incoming_event, on_response)
            try:
                # wait until on_response callback is called or we run into 10 sec timeout
                socketIO.wait(10)
            except StopWaitingException:
                pass
        return received_data

    def test_connection_not_authenticated(self):
        with self.assertRaises(ConnectionError):
            SocketIO('localhost', self.APP_PORT, wait_for_connection=False)

    def test_connection_authenticated(self):
        # log in
        r = requests.post("http://localhost:{}/auth/login"
                          .format(self.APP_PORT), data=self.test_user)
        self.assertEqual(r.status_code, 200)

        # check connection
        with SocketIO('localhost', self.APP_PORT,
                      cookies={'session': r.cookies['session']},
                      wait_for_connection=False) as socketIO:
            self.assertTrue(socketIO.connected)

    def test_echo(self):
        expected_data = {"test_key": "test_value"}
        received_data = self.send_message('echo', 'echo_response', expected_data)
        self.assertEqual(received_data, expected_data)
