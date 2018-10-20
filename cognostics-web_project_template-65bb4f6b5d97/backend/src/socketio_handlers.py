import logging
from functools import wraps

from flask import session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect


def user_is_authenticated():
    return "username" in session


def authenticated_only(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if user_is_authenticated():
            return f(*args, **kwargs)
        else:
            disconnect()
    return wrapped


def create_sio(request_handler):
    sio = SocketIO(engineio_logger=True, logger=True)

    @sio.on('connect')
    def handle_connect():
        logging.info('SocketIO Connect')
        return user_is_authenticated()

    @sio.on('disconnect')
    def handle_disconnect():
        logging.info('SocketIO Disconnect')
        pass

    @sio.on('request')
    @authenticated_only
    def handle_sio_request(data):
        # to be able to handle all requests asynchronously we create a separate thread
        # for each of the requests, but in order to be able to access database
        # we need to have flask app context. For that reason handle_async_request
        # function is created - it is wrapped in "copy_current_request_context"
        # and therefore has app context. We pass this function further into request handler
        # where it is called
        @copy_current_request_context
        def handle_async_request(handle_request, method, request, username):
            response = handle_request(method, request, username)
            emit("response", response)

        response = request_handler.handle_request(data, session["username"], handle_async_request)
        if response is not None:
            emit("response", response)

    @sio.on('echo')
    @authenticated_only
    def echo(data):
        logging.info('echo')
        emit("echo_response", data)

    return sio
