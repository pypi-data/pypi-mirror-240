# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.stock import route_pb2 as v1_dot_stock_dot_route__pb2


class RouteServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RouteCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteCreate",
            request_serializer=v1_dot_stock_dot_route__pb2.RouteCreateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_route__pb2.RouteCreateResponse.FromString,
        )
        self.RouteRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteRead",
            request_serializer=v1_dot_stock_dot_route__pb2.RouteReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_route__pb2.RouteReadResponse.FromString,
        )
        self.RouteUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteUpdate",
            request_serializer=v1_dot_stock_dot_route__pb2.RouteUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_route__pb2.RouteUpdateResponse.FromString,
        )
        self.RouteDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteDelete",
            request_serializer=v1_dot_stock_dot_route__pb2.RouteDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_route__pb2.RouteDeleteResponse.FromString,
        )


class RouteServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RouteCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RouteRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RouteUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RouteDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RouteServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "RouteCreate": grpc.unary_unary_rpc_method_handler(
            servicer.RouteCreate,
            request_deserializer=v1_dot_stock_dot_route__pb2.RouteCreateRequest.FromString,
            response_serializer=v1_dot_stock_dot_route__pb2.RouteCreateResponse.SerializeToString,
        ),
        "RouteRead": grpc.unary_unary_rpc_method_handler(
            servicer.RouteRead,
            request_deserializer=v1_dot_stock_dot_route__pb2.RouteReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_route__pb2.RouteReadResponse.SerializeToString,
        ),
        "RouteUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.RouteUpdate,
            request_deserializer=v1_dot_stock_dot_route__pb2.RouteUpdateRequest.FromString,
            response_serializer=v1_dot_stock_dot_route__pb2.RouteUpdateResponse.SerializeToString,
        ),
        "RouteDelete": grpc.unary_unary_rpc_method_handler(
            servicer.RouteDelete,
            request_deserializer=v1_dot_stock_dot_route__pb2.RouteDeleteRequest.FromString,
            response_serializer=v1_dot_stock_dot_route__pb2.RouteDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.route.RouteService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RouteService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RouteCreate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteCreate",
            v1_dot_stock_dot_route__pb2.RouteCreateRequest.SerializeToString,
            v1_dot_stock_dot_route__pb2.RouteCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RouteRead(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteRead",
            v1_dot_stock_dot_route__pb2.RouteReadRequest.SerializeToString,
            v1_dot_stock_dot_route__pb2.RouteReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RouteUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteUpdate",
            v1_dot_stock_dot_route__pb2.RouteUpdateRequest.SerializeToString,
            v1_dot_stock_dot_route__pb2.RouteUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RouteDelete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.stock.route.RouteService/RouteDelete",
            v1_dot_stock_dot_route__pb2.RouteDeleteRequest.SerializeToString,
            v1_dot_stock_dot_route__pb2.RouteDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
