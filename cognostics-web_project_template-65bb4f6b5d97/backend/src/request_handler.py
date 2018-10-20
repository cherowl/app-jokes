import logging

import eventlet

import src.models as models


class ErrorWithStatusMessage(Exception):
    pass


class RequestHandler:

    def handle_request(self, request, username, handle_async_request_wrapper):
        logging.info("Socket request from {}: {}".format(username, request))

        if "id" in request and "type" in request and request["type"] in self.requests:
            request_method = self.requests[request["type"]]
            eventlet.spawn_n(handle_async_request_wrapper, self.handle_async_request,
                             request_method, request, username)
            response = None
        else:
            response = {**request, "status": "fail", "message": "Invalid/Unknown Request"}

        return response

    def handle_async_request(self, request_method, request, username):
        response = {"id": request["id"], "type": request["type"]}
        try:
            data = request.get("data", {})
            response_data = request_method(self, data, username)
            response["status"] = "success"
            response["data"] = response_data

        except ErrorWithStatusMessage as error:
            response["status"] = "fail"
            response["message"] = "{}".format(error)

        except Exception as e:
            logging.error(str(e), exc_info=True)
            response["status"] = "fail"

        return response

    def get_user_full_name(self, data, username):
        user = models.User.query.filter(models.User.username == username).one()
        return user.get_full_name()

    # all allowed requests
    requests = {
        "get_user_full_name": get_user_full_name,
    }
