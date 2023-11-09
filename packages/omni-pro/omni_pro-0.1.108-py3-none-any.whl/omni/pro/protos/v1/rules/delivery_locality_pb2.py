# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/delivery_locality.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni.pro.protos.common import base_pb2 as common_dot_base__pb2
from omni.pro.protos.v1.rules import country_pb2 as v1_dot_rules_dot_country__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n v1/rules/delivery_locality.proto\x12+pro.omni.oms.api.v1.rules.delivery_locality\x1a\x11\x63ommon/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x16v1/rules/country.proto"\x9a\x02\n\x10\x44\x65liveryLocality\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\x07\x63ountry\x18\x03 \x01(\x0b\x32*.pro.omni.oms.api.v1.rules.country.Country\x12\x17\n\x0f\x63ode_collection\x18\x04 \x01(\t\x12)\n\x05items\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12*\n\x06\x61\x63tive\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x07 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xa1\x01\n\x1d\x44\x65liveryLocalityCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncountry_id\x18\x02 \x01(\t\x12\x17\n\x0f\x63ode_collection\x18\x03 \x01(\t\x12\r\n\x05items\x18\x04 \x03(\t\x12\x36\n\x07\x63ontext\x18\x05 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc5\x01\n\x1e\x44\x65liveryLocalityCreateResponse\x12X\n\x11\x64\x65livery_locality\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocality\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf9\x02\n\x1b\x44\x65liveryLocalityReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x80\x02\n\x1c\x44\x65liveryLocalityReadResponse\x12Z\n\x13\x64\x65livery_localities\x18\x01 \x03(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocality\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xb1\x01\n\x1d\x44\x65liveryLocalityUpdateRequest\x12X\n\x11\x64\x65livery_locality\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocality\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc5\x01\n\x1e\x44\x65liveryLocalityUpdateResponse\x12X\n\x11\x64\x65livery_locality\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocality\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"c\n\x1d\x44\x65liveryLocalityDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"k\n\x1e\x44\x65liveryLocalityDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xeb\x05\n\x17\x44\x65liveryLocalityService\x12\xb3\x01\n\x16\x44\x65liveryLocalityCreate\x12J.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityCreateRequest\x1aK.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityCreateResponse"\x00\x12\xad\x01\n\x14\x44\x65liveryLocalityRead\x12H.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityReadRequest\x1aI.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityReadResponse"\x00\x12\xb3\x01\n\x16\x44\x65liveryLocalityUpdate\x12J.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityUpdateRequest\x1aK.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityUpdateResponse"\x00\x12\xb3\x01\n\x16\x44\x65liveryLocalityDelete\x12J.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityDeleteRequest\x1aK.pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityDeleteResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.delivery_locality_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_DELIVERYLOCALITY"]._serialized_start = 187
    _globals["_DELIVERYLOCALITY"]._serialized_end = 469
    _globals["_DELIVERYLOCALITYCREATEREQUEST"]._serialized_start = 472
    _globals["_DELIVERYLOCALITYCREATEREQUEST"]._serialized_end = 633
    _globals["_DELIVERYLOCALITYCREATERESPONSE"]._serialized_start = 636
    _globals["_DELIVERYLOCALITYCREATERESPONSE"]._serialized_end = 833
    _globals["_DELIVERYLOCALITYREADREQUEST"]._serialized_start = 836
    _globals["_DELIVERYLOCALITYREADREQUEST"]._serialized_end = 1213
    _globals["_DELIVERYLOCALITYREADRESPONSE"]._serialized_start = 1216
    _globals["_DELIVERYLOCALITYREADRESPONSE"]._serialized_end = 1472
    _globals["_DELIVERYLOCALITYUPDATEREQUEST"]._serialized_start = 1475
    _globals["_DELIVERYLOCALITYUPDATEREQUEST"]._serialized_end = 1652
    _globals["_DELIVERYLOCALITYUPDATERESPONSE"]._serialized_start = 1655
    _globals["_DELIVERYLOCALITYUPDATERESPONSE"]._serialized_end = 1852
    _globals["_DELIVERYLOCALITYDELETEREQUEST"]._serialized_start = 1854
    _globals["_DELIVERYLOCALITYDELETEREQUEST"]._serialized_end = 1953
    _globals["_DELIVERYLOCALITYDELETERESPONSE"]._serialized_start = 1955
    _globals["_DELIVERYLOCALITYDELETERESPONSE"]._serialized_end = 2062
    _globals["_DELIVERYLOCALITYSERVICE"]._serialized_start = 2065
    _globals["_DELIVERYLOCALITYSERVICE"]._serialized_end = 2812
# @@protoc_insertion_point(module_scope)
