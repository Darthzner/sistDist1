# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import search_pb2 as search__pb2


class SearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProds = channel.unary_unary(
                '/search.Search/GetProds',
                request_serializer=search__pb2.Product.SerializeToString,
                response_deserializer=search__pb2.ProductInfo.FromString,
                )


class SearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProds': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProds,
                    request_deserializer=search__pb2.Product.FromString,
                    response_serializer=search__pb2.ProductInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'search.Search', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Search(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/search.Search/GetProds',
            search__pb2.Product.SerializeToString,
            search__pb2.ProductInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)