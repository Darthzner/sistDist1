import grpc
from concurrent import futures
import time
import json
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2


class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetProds(self, request, context):
        print(request.name)
        message = request.name
        print('Hello I am up and running received ',message,' message from you')

        #cargar lista de productos
        resultList = []
        
        with open("../Inventario/inventario.json") as allProds:
            
            jsonObject = json.load(allProds)
            
            for item in jsonObject['products_list']:
                
                if item['name'].find(message) != -1:
                    resultTemp = {                   
                        'name' : item['name'],
                        'price': item['price'],
                        'stock': item['stock']
                    }
                    resultList.append(resultTemp)
                    resultTemp = ""


        search_res = {'item': resultList}
        
        
        var = pb2.ProductInfo(**search_res)
     
        return var


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
    print('CORRIENDO')