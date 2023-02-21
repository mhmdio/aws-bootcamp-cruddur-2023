import os
import logging
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask import got_request_exception
import rollbar
import rollbar.contrib.flask
from services.create_activity import *
from services.create_message import *
from services.create_reply import *
from services.home_activities import *
from services.notifications_activities import *
from services.message_groups import *
from services.messages import *
from services.search_activities import *
from services.show_activity import *
from services.user_activities import *

app = Flask(__name__)
frontend = os.getenv("FRONTEND_URL")
backend = os.getenv("BACKEND_URL")
origins = [frontend, backend]
cors = CORS(
    app,
    # resources={r"/api/*": {"origins": "*"}},
    resources={r"/api/*": {"origins": origins}},
    expose_headers="location,link",
    # expose_headers="*",
    allow_headers="content-type,if-modified-since",
    # allow_headers="*",
    methods="OPTIONS,GET,HEAD,POST",
)


@app.before_first_request
def init_rollbar():
    rollbar.init(os.getenv("ROLLBAR_ACCESS_TOKEN"), environment='development')
    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

@app.route('/healthz')
def healthz():
    return '\nHealthy!\n\n', 200

@app.route("/api/message_groups", methods=["GET"])
def data_message_groups():
    user_handle = "Mohammed"
    model = MessageGroups.run(user_handle=user_handle)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200


@app.route("/api/messages/@<string:handle>", methods=["GET"])
def data_messages(handle):
    user_sender_handle = "Mohammed"
    user_receiver_handle = request.args.get("user_reciever_handle")

    model = Messages.run(
        user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle
    )
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/messages", methods=["POST", "OPTIONS"])
@cross_origin()
def data_create_message():
    user_sender_handle = "Mohammed"
    user_receiver_handle = request.json["user_receiver_handle"]
    message = request.json["message"]

    model = CreateMessage.run(
        message=message,
        user_sender_handle=user_sender_handle,
        user_receiver_handle=user_receiver_handle,
    )
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/activities/home", methods=["GET"])
def data_home():
    data = HomeActivities.run()
    return data, 200


@app.route("/api/activities/notifications", methods=["GET"])
def data_notifications():
    data = NotificationsActivities.run()
    return data, 200


@app.route("/api/activities/@<string:handle>", methods=["GET"])
def data_handle(handle):
    model = UserActivities.run(handle)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200


@app.route("/api/activities/search", methods=["GET"])
def data_search():
    term = request.args.get("term")
    model = SearchActivities.run(term)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/activities", methods=["POST", "OPTIONS"])
@cross_origin()
def data_activities():
    user_handle = "mohammed"
    message = request.json["message"]
    ttl = request.json["ttl"]
    model = CreateActivity.run(message, user_handle, ttl)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


@app.route("/api/activities/<string:activity_uuid>", methods=["GET"])
def data_show_activity(activity_uuid):
    data = ShowActivity.run(activity_uuid=activity_uuid)
    return data, 200


@app.route("/api/activities/<string:activity_uuid>/reply", methods=["POST", "OPTIONS"])
@cross_origin()
def data_activities_reply(activity_uuid):
    user_handle = "mohammed"
    message = request.json["message"]
    model = CreateReply.run(message, user_handle, activity_uuid)
    if model["errors"] is not None:
        return model["errors"], 422
    else:
        return model["data"], 200
    return


if __name__ == "__main__":
    app.run(debug=True)
