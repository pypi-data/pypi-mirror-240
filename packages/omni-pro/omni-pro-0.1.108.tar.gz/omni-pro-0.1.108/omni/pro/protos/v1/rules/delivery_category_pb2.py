# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/delivery_category.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni.pro.protos.common import base_pb2 as common_dot_base__pb2
from omni.pro.protos.v1.rules import category_pb2 as v1_dot_rules_dot_category__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n v1/rules/delivery_category.proto\x12+pro.omni.oms.api.v1.rules.delivery_category\x1a\x11\x63ommon/base.proto\x1a\x17v1/rules/category.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xdb\x01\n\x10\x44\x65liveryCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12@\n\ncategories\x18\x03 \x03(\x0b\x32,.pro.omni.oms.api.v1.rules.category.Category\x12*\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"}\n\x1d\x44\x65liveryCategoryCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x61tegory_codes\x18\x02 \x03(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc5\x01\n\x1e\x44\x65liveryCategoryCreateResponse\x12X\n\x11\x64\x65livery_category\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf9\x02\n\x1b\x44\x65liveryCategoryReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\t\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x80\x02\n\x1c\x44\x65liveryCategoryReadResponse\x12Z\n\x13\x64\x65livery_categories\x18\x01 \x03(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xb1\x01\n\x1d\x44\x65liveryCategoryUpdateRequest\x12X\n\x11\x64\x65livery_category\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xc5\x01\n\x1e\x44\x65liveryCategoryUpdateResponse\x12X\n\x11\x64\x65livery_category\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"c\n\x1d\x44\x65liveryCategoryDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"k\n\x1e\x44\x65liveryCategoryDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x82\x01\n\x12\x41\x64\x64\x43\x61tegoryRequest\x12\x1c\n\x14\x64\x65livery_category_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x61tegory_codes\x18\x02 \x03(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xba\x01\n\x13\x41\x64\x64\x43\x61tegoryResponse\x12X\n\x11\x64\x65livery_category\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x85\x01\n\x15RemoveCategoryRequest\x12\x1c\n\x14\x64\x65livery_category_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x61tegory_codes\x18\x02 \x03(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xbd\x01\n\x16RemoveCategoryResponse\x12X\n\x11\x64\x65livery_category\x18\x01 \x01(\x0b\x32=.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategory\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x9e\x08\n\x17\x44\x65liveryCategoryService\x12\xb3\x01\n\x16\x44\x65liveryCategoryCreate\x12J.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryCreateRequest\x1aK.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryCreateResponse"\x00\x12\xad\x01\n\x14\x44\x65liveryCategoryRead\x12H.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryReadRequest\x1aI.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryReadResponse"\x00\x12\xb3\x01\n\x16\x44\x65liveryCategoryUpdate\x12J.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryUpdateRequest\x1aK.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryUpdateResponse"\x00\x12\xb3\x01\n\x16\x44\x65liveryCategoryDelete\x12J.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryDeleteRequest\x1aK.pro.omni.oms.api.v1.rules.delivery_category.DeliveryCategoryDeleteResponse"\x00\x12\x92\x01\n\x0b\x41\x64\x64\x43\x61tegory\x12?.pro.omni.oms.api.v1.rules.delivery_category.AddCategoryRequest\x1a@.pro.omni.oms.api.v1.rules.delivery_category.AddCategoryResponse"\x00\x12\x9b\x01\n\x0eRemoveCategory\x12\x42.pro.omni.oms.api.v1.rules.delivery_category.RemoveCategoryRequest\x1a\x43.pro.omni.oms.api.v1.rules.delivery_category.RemoveCategoryResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.delivery_category_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_DELIVERYCATEGORY"]._serialized_start = 158
    _globals["_DELIVERYCATEGORY"]._serialized_end = 377
    _globals["_DELIVERYCATEGORYCREATEREQUEST"]._serialized_start = 379
    _globals["_DELIVERYCATEGORYCREATEREQUEST"]._serialized_end = 504
    _globals["_DELIVERYCATEGORYCREATERESPONSE"]._serialized_start = 507
    _globals["_DELIVERYCATEGORYCREATERESPONSE"]._serialized_end = 704
    _globals["_DELIVERYCATEGORYREADREQUEST"]._serialized_start = 707
    _globals["_DELIVERYCATEGORYREADREQUEST"]._serialized_end = 1084
    _globals["_DELIVERYCATEGORYREADRESPONSE"]._serialized_start = 1087
    _globals["_DELIVERYCATEGORYREADRESPONSE"]._serialized_end = 1343
    _globals["_DELIVERYCATEGORYUPDATEREQUEST"]._serialized_start = 1346
    _globals["_DELIVERYCATEGORYUPDATEREQUEST"]._serialized_end = 1523
    _globals["_DELIVERYCATEGORYUPDATERESPONSE"]._serialized_start = 1526
    _globals["_DELIVERYCATEGORYUPDATERESPONSE"]._serialized_end = 1723
    _globals["_DELIVERYCATEGORYDELETEREQUEST"]._serialized_start = 1725
    _globals["_DELIVERYCATEGORYDELETEREQUEST"]._serialized_end = 1824
    _globals["_DELIVERYCATEGORYDELETERESPONSE"]._serialized_start = 1826
    _globals["_DELIVERYCATEGORYDELETERESPONSE"]._serialized_end = 1933
    _globals["_ADDCATEGORYREQUEST"]._serialized_start = 1936
    _globals["_ADDCATEGORYREQUEST"]._serialized_end = 2066
    _globals["_ADDCATEGORYRESPONSE"]._serialized_start = 2069
    _globals["_ADDCATEGORYRESPONSE"]._serialized_end = 2255
    _globals["_REMOVECATEGORYREQUEST"]._serialized_start = 2258
    _globals["_REMOVECATEGORYREQUEST"]._serialized_end = 2391
    _globals["_REMOVECATEGORYRESPONSE"]._serialized_start = 2394
    _globals["_REMOVECATEGORYRESPONSE"]._serialized_end = 2583
    _globals["_DELIVERYCATEGORYSERVICE"]._serialized_start = 2586
    _globals["_DELIVERYCATEGORYSERVICE"]._serialized_end = 3640
# @@protoc_insertion_point(module_scope)
