import redis
import grpc, grpc_tools
import json
from flask import Flask,  jsonify
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


@app.route('/api/getprod',methods=['GET'])
def get_prods():
    with open("../Inventario/inventario.json") as prods:
        jsonObject = json.load(prods)
        prods.close()
        return jsonify(jsonObject['products_list'])
    




if __name__ == '__main__':
    app.run(debug=True)
""" 
r = redis.Redis(host='localhost', port=6379, db=0)

r.set("hello1",json.dumps({"nombre" : "dimeloMa"}))

value = r.get('hello1')

print(value) """