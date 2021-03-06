# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc_basic import collect_pb2 as collect__pb2


class CollectorStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CollectImage = channel.unary_unary(
                '/Collector/CollectImage',
                request_serializer=collect__pb2.Empty.SerializeToString,
                response_deserializer=collect__pb2.ImageInfo.FromString,
                )


class CollectorServicer(object):
    """The greeting service definition.
    """

    def CollectImage(self, request, context):
        """Receive the request to collect a new image using the camera;
        store the image in S3 and return the information of that image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CollectImage': grpc.unary_unary_rpc_method_handler(
                    servicer.CollectImage,
                    request_deserializer=collect__pb2.Empty.FromString,
                    response_serializer=collect__pb2.ImageInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Collector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Collector(object):
    """The greeting service definition.
    """

    @staticmethod
    def CollectImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Collector/CollectImage',
            collect__pb2.Empty.SerializeToString,
            collect__pb2.ImageInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
