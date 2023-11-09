# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/sale.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from omni.pro.protos.common import base_pb2 as common_dot_base__pb2
from omni.pro.protos.v1.sales import address_pb2 as v1_dot_sales_dot_address__pb2
from omni.pro.protos.v1.sales import channel_pb2 as v1_dot_sales_dot_channel__pb2
from omni.pro.protos.v1.sales import client_pb2 as v1_dot_sales_dot_client__pb2
from omni.pro.protos.v1.sales import country_pb2 as v1_dot_sales_dot_country__pb2
from omni.pro.protos.v1.sales import currency_pb2 as v1_dot_sales_dot_currency__pb2
from omni.pro.protos.v1.sales import state_pb2 as v1_dot_sales_dot_state__pb2
from omni.pro.protos.v1.sales import warehouse_pb2 as v1_dot_sales_dot_warehouse__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13v1/sales/sale.proto\x12\x1epro.omni.oms.api.v1.sales.sale\x1a\x11\x63ommon/base.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x16v1/sales/country.proto\x1a\x17v1/sales/currency.proto\x1a\x15v1/sales/client.proto\x1a\x16v1/sales/address.proto\x1a\x18v1/sales/warehouse.proto\x1a\x14v1/sales/state.proto\x1a\x16v1/sales/channel.proto"\xc3\x05\n\x04Sale\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ndate_order\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06origin\x18\x04 \x01(\t\x12;\n\x07\x63hannel\x18\x05 \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.channel.Channel\x12>\n\x08\x63urrency\x18\x06 \x01(\x0b\x32,.pro.omni.oms.api.v1.sales.currency.Currency\x12\x30\n\x0c\x63onfirm_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x06\x63lient\x18\x08 \x01(\x0b\x32(.pro.omni.oms.api.v1.sales.client.Client\x12@\n\x0c\x62ill_address\x18\t \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.address.Address\x12;\n\x07\x63ountry\x18\n \x01(\x0b\x32*.pro.omni.oms.api.v1.sales.country.Country\x12\x41\n\twarehouse\x18\x0b \x01(\x0b\x32..pro.omni.oms.api.v1.sales.warehouse.Warehouse\x12\x12\n\njson_order\x18\x0c \x01(\t\x12\x35\n\x05state\x18\r \x01(\x0b\x32&.pro.omni.oms.api.v1.sales.state.State\x12*\n\x06\x61\x63tive\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x0cobject_audit\x18\x0f \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xa1\x02\n\x0fSaleIntegration\x12.\n\rorder_details\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\toms_rules\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12/\n\x0e\x63lient_details\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07payment\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0border_items\x18\x05 \x03(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08shipping\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct"\xf2\x02\n\x11SaleCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\ndate_order\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\x12\n\nchannel_id\x18\x04 \x01(\x05\x12\x13\n\x0b\x63urrency_id\x18\x05 \x01(\t\x12\x30\n\x0c\x63onfirm_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tclient_id\x18\x07 \x01(\t\x12\x12\n\ncountry_id\x18\x08 \x01(\t\x12\x19\n\x11\x62ill_address_code\x18\t \x01(\t\x12\x14\n\x0cwarehouse_id\x18\n \x01(\x05\x12\x12\n\njson_order\x18\x0b \x01(\t\x12\x10\n\x08state_id\x18\x0c \x01(\x05\x12\x36\n\x07\x63ontext\x18\r \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x01\n\x12SaleCreateResponse\x12\x32\n\x04sale\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.sale.Sale\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xed\x02\n\x0fSaleReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xcc\x01\n\x10SaleReadResponse\x12\x32\n\x04sale\x18\x01 \x03(\x0b\x32$.pro.omni.oms.api.v1.sales.sale.Sale\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData"\x7f\n\x11SaleUpdateRequest\x12\x32\n\x04sale\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.sale.Sale\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x93\x01\n\x12SaleUpdateResponse\x12\x32\n\x04sale\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.sale.Sale\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"W\n\x11SaleDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"_\n\x12SaleDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xa1\x01\n\x1cSaleCreateIntegrationRequest\x12I\n\x10sale_integration\x18\x01 \x01(\x0b\x32/.pro.omni.oms.api.v1.sales.sale.SaleIntegration\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9e\x01\n\x1dSaleCreateIntegrationResponse\x12\x32\n\x04sale\x18\x01 \x01(\x0b\x32$.pro.omni.oms.api.v1.sales.sale.Sale\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xfc\x04\n\x0bSaleService\x12u\n\nSaleCreate\x12\x31.pro.omni.oms.api.v1.sales.sale.SaleCreateRequest\x1a\x32.pro.omni.oms.api.v1.sales.sale.SaleCreateResponse"\x00\x12o\n\x08SaleRead\x12/.pro.omni.oms.api.v1.sales.sale.SaleReadRequest\x1a\x30.pro.omni.oms.api.v1.sales.sale.SaleReadResponse"\x00\x12u\n\nSaleUpdate\x12\x31.pro.omni.oms.api.v1.sales.sale.SaleUpdateRequest\x1a\x32.pro.omni.oms.api.v1.sales.sale.SaleUpdateResponse"\x00\x12u\n\nSaleDelete\x12\x31.pro.omni.oms.api.v1.sales.sale.SaleDeleteRequest\x1a\x32.pro.omni.oms.api.v1.sales.sale.SaleDeleteResponse"\x00\x12\x96\x01\n\x15SaleCreateIntegration\x12<.pro.omni.oms.api.v1.sales.sale.SaleCreateIntegrationRequest\x1a=.pro.omni.oms.api.v1.sales.sale.SaleCreateIntegrationResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.sale_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_SALE"]._serialized_start = 338
    _globals["_SALE"]._serialized_end = 1045
    _globals["_SALEINTEGRATION"]._serialized_start = 1048
    _globals["_SALEINTEGRATION"]._serialized_end = 1337
    _globals["_SALECREATEREQUEST"]._serialized_start = 1340
    _globals["_SALECREATEREQUEST"]._serialized_end = 1710
    _globals["_SALECREATERESPONSE"]._serialized_start = 1713
    _globals["_SALECREATERESPONSE"]._serialized_end = 1860
    _globals["_SALEREADREQUEST"]._serialized_start = 1863
    _globals["_SALEREADREQUEST"]._serialized_end = 2228
    _globals["_SALEREADRESPONSE"]._serialized_start = 2231
    _globals["_SALEREADRESPONSE"]._serialized_end = 2435
    _globals["_SALEUPDATEREQUEST"]._serialized_start = 2437
    _globals["_SALEUPDATEREQUEST"]._serialized_end = 2564
    _globals["_SALEUPDATERESPONSE"]._serialized_start = 2567
    _globals["_SALEUPDATERESPONSE"]._serialized_end = 2714
    _globals["_SALEDELETEREQUEST"]._serialized_start = 2716
    _globals["_SALEDELETEREQUEST"]._serialized_end = 2803
    _globals["_SALEDELETERESPONSE"]._serialized_start = 2805
    _globals["_SALEDELETERESPONSE"]._serialized_end = 2900
    _globals["_SALECREATEINTEGRATIONREQUEST"]._serialized_start = 2903
    _globals["_SALECREATEINTEGRATIONREQUEST"]._serialized_end = 3064
    _globals["_SALECREATEINTEGRATIONRESPONSE"]._serialized_start = 3067
    _globals["_SALECREATEINTEGRATIONRESPONSE"]._serialized_end = 3225
    _globals["_SALESERVICE"]._serialized_start = 3228
    _globals["_SALESERVICE"]._serialized_end = 3864
# @@protoc_insertion_point(module_scope)
