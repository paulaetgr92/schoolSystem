import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello, World!")

def handler(event, context):
    from flask import Request
    from werkzeug.wrappers import Response

    environ = {
        "REQUEST_METHOD": event["httpMethod"],
        "PATH_INFO": event["path"],
        "QUERY_STRING": event.get("queryStringParameters", ""),
        "wsgi.input": event["body"],
        "SERVER_NAME": os.getenv("SERVER_NAME", "localhost"),
        "SERVER_PORT": os.getenv("SERVER_PORT", 80),
        **event["headers"],
    }

    response = app.full_dispatch_request()
    return {
        "statusCode": 200,
        "body": response.get_data(as_text=True),
        "headers": {
            "Content-Type": "application/json"
        }
    }
