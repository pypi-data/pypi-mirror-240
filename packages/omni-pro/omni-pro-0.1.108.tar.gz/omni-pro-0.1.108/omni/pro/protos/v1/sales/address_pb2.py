# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni.pro.protos.common import base_pb2 as common_dot_base__pb2
from omni.pro.protos.v1.sales import client_pb2 as v1_dot_sales_dot_client__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16v1/sales/address.proto\x12!pro.omni.oms.api.v1.sales.address\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x15v1/sales/client.proto"\x86\x02\n\x07\x41\x64\x64ress\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x38\n\x06\x63lient\x18\x02 \x01(\x0b\x32(.pro.omni.oms.api.v1.sales.client.Client\x12\x16\n\x0e\x61\x64\x64ress_doc_id\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x64\x64ress_code\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12*\n\x06\x61\x63tive\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x08 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xab\x01\n\x14\x41\x64\x64ressCreateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x16\n\x0e\x61\x64\x64ress_doc_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x64\x64ress_code\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x36\n\x07\x63ontext\x18\x06 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x41\x64\x64ressCreateResponse\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.address.Address\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf0\x02\n\x12\x41\x64\x64ressReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xda\x01\n\x13\x41\x64\x64ressReadResponse\x12=\n\taddresses\x18\x01 \x03(\x0b\x32*.pro.omni.oms.api.v1.sales.address.Address\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x8b\x01\n\x14\x41\x64\x64ressUpdateRequest\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.address.Address\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x41\x64\x64ressUpdateResponse\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.address.Address\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"Z\n\x14\x41\x64\x64ressDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15\x41\x64\x64ressDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa5\x04\n\x0e\x41\x64\x64ressService\x12\x84\x01\n\rAddressCreate\x12\x37.pro.omni.oms.api.v1.sales.address.AddressCreateRequest\x1a\x38.pro.omni.oms.api.v1.sales.address.AddressCreateResponse"\x00\x12~\n\x0b\x41\x64\x64ressRead\x12\x35.pro.omni.oms.api.v1.sales.address.AddressReadRequest\x1a\x36.pro.omni.oms.api.v1.sales.address.AddressReadResponse"\x00\x12\x84\x01\n\rAddressUpdate\x12\x37.pro.omni.oms.api.v1.sales.address.AddressUpdateRequest\x1a\x38.pro.omni.oms.api.v1.sales.address.AddressUpdateResponse"\x00\x12\x84\x01\n\rAddressDelete\x12\x37.pro.omni.oms.api.v1.sales.address.AddressDeleteRequest\x1a\x38.pro.omni.oms.api.v1.sales.address.AddressDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.address_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_ADDRESS"]._serialized_start = 136
    _globals["_ADDRESS"]._serialized_end = 398
    _globals["_ADDRESSCREATEREQUEST"]._serialized_start = 401
    _globals["_ADDRESSCREATEREQUEST"]._serialized_end = 572
    _globals["_ADDRESSCREATERESPONSE"]._serialized_start = 575
    _globals["_ADDRESSCREATERESPONSE"]._serialized_end = 734
    _globals["_ADDRESSREADREQUEST"]._serialized_start = 737
    _globals["_ADDRESSREADREQUEST"]._serialized_end = 1105
    _globals["_ADDRESSREADRESPONSE"]._serialized_start = 1108
    _globals["_ADDRESSREADRESPONSE"]._serialized_end = 1326
    _globals["_ADDRESSUPDATEREQUEST"]._serialized_start = 1329
    _globals["_ADDRESSUPDATEREQUEST"]._serialized_end = 1468
    _globals["_ADDRESSUPDATERESPONSE"]._serialized_start = 1471
    _globals["_ADDRESSUPDATERESPONSE"]._serialized_end = 1630
    _globals["_ADDRESSDELETEREQUEST"]._serialized_start = 1632
    _globals["_ADDRESSDELETEREQUEST"]._serialized_end = 1722
    _globals["_ADDRESSDELETERESPONSE"]._serialized_start = 1724
    _globals["_ADDRESSDELETERESPONSE"]._serialized_end = 1822
    _globals["_ADDRESSSERVICE"]._serialized_start = 1825
    _globals["_ADDRESSSERVICE"]._serialized_end = 2374
# @@protoc_insertion_point(module_scope)
