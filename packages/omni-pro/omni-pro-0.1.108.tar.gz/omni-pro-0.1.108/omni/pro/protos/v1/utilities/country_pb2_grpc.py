# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.utilities import country_pb2 as v1_dot_utilities_dot_country__pb2


class CountryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CountryCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryCreate",
            request_serializer=v1_dot_utilities_dot_country__pb2.CountryCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_country__pb2.CountryCreateResponse.FromString,
        )
        self.CountryRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryRead",
            request_serializer=v1_dot_utilities_dot_country__pb2.CountryReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_country__pb2.CountryReadResponse.FromString,
        )
        self.CountryUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryUpdate",
            request_serializer=v1_dot_utilities_dot_country__pb2.CountryUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_country__pb2.CountryUpdateResponse.FromString,
        )
        self.CountryDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryDelete",
            request_serializer=v1_dot_utilities_dot_country__pb2.CountryDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_country__pb2.CountryDeleteResponse.FromString,
        )


class CountryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CountryCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CountryRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CountryUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CountryDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CountryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CountryCreate": grpc.unary_unary_rpc_method_handler(
            servicer.CountryCreate,
            request_deserializer=v1_dot_utilities_dot_country__pb2.CountryCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_country__pb2.CountryCreateResponse.SerializeToString,
        ),
        "CountryRead": grpc.unary_unary_rpc_method_handler(
            servicer.CountryRead,
            request_deserializer=v1_dot_utilities_dot_country__pb2.CountryReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_country__pb2.CountryReadResponse.SerializeToString,
        ),
        "CountryUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.CountryUpdate,
            request_deserializer=v1_dot_utilities_dot_country__pb2.CountryUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_country__pb2.CountryUpdateResponse.SerializeToString,
        ),
        "CountryDelete": grpc.unary_unary_rpc_method_handler(
            servicer.CountryDelete,
            request_deserializer=v1_dot_utilities_dot_country__pb2.CountryDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_country__pb2.CountryDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.country.CountryService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class CountryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CountryCreate(
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
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryCreate",
            v1_dot_utilities_dot_country__pb2.CountryCreateRequest.SerializeToString,
            v1_dot_utilities_dot_country__pb2.CountryCreateResponse.FromString,
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
    def CountryRead(
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
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryRead",
            v1_dot_utilities_dot_country__pb2.CountryReadRequest.SerializeToString,
            v1_dot_utilities_dot_country__pb2.CountryReadResponse.FromString,
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
    def CountryUpdate(
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
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryUpdate",
            v1_dot_utilities_dot_country__pb2.CountryUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_country__pb2.CountryUpdateResponse.FromString,
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
    def CountryDelete(
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
            "/pro.omni.oms.api.v1.utilities.country.CountryService/CountryDelete",
            v1_dot_utilities_dot_country__pb2.CountryDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_country__pb2.CountryDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
