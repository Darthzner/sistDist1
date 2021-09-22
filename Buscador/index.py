import redis
import grpc, grpc_tools
import json
from flask import Flask,  jsonify
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
from google.protobuf.json_format import MessageToJson


#python -m grpc_tools.protoc (protocol buffer) --proto_path=. ./search.proto --python_out=. --grpc_python_out=.
class SearchClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
       

        # instantiate a channel
        self.channel = grpc.insecure_channel('localhost:50051' ,options=(('grpc.enable_http_proxy', 0),))

        # bind the client and the server
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetProds
        """
       
        message = pb2.Product(name=message)
        print(message)
        
    
        variable = self.stub.GetProds(message)
       
        return variable

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


@app.route('/api/getprod/<pname>',methods=['GET'])
def get_prods(pname):
    #with open("../Inventario/inventario.json") as prods:
        #jsonObject = json.load(prods)
        #prods.close()
    re = redis.Redis()    
    objectt = re.get(pname)
    if objectt != None:
        new = objectt.decode('utf-8').replace("'", '"')
        print('entreaca: ',new)
        data = json.loads(new)
        re.close()
        return json.dumps(data, indent=4, sort_keys=True)
    
    else:       
       
        client = SearchClient()        
        result = client.get_url(message=pname)        
        val = MessageToJson(result)
        re.set(pname,val)
        re.close()
        return MessageToJson(result)
       # print(result)
          

    
    
       
    

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.config_set('maxmemory', '100mb')
    r.config_set('maxmemory-policy', 'allkeys-lru')
    
    
    app.run(debug=True)



