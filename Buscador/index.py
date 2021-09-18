import redis
import json
from flask import Flask,  jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

api = Api(app)
api.prefix = '/api'

r = redis.Redis(host='localhost', port=6379, db=0)

r.set("hello1",json.dumps({"nombre" : "dimeloMa"}))

value = r.get('hello1')

print(value)