# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: csci4220_hw4.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'csci4220_hw4.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x63sci4220_hw4.proto\"1\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"@\n\x08NodeList\x12\x1e\n\x0fresponding_node\x18\x01 \x01(\x0b\x32\x05.Node\x12\x14\n\x05nodes\x18\x02 \x03(\x0b\x32\x05.Node\"+\n\x05IDKey\x12\x13\n\x04node\x18\x01 \x01(\x0b\x32\x05.Node\x12\r\n\x05idkey\x18\x02 \x01(\r\";\n\x08KeyValue\x12\x13\n\x04node\x18\x01 \x01(\x0b\x32\x05.Node\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\"o\n\x0fKV_Node_Wrapper\x12\x1e\n\x0fresponding_node\x18\x01 \x01(\x0b\x32\x05.Node\x12\x0f\n\x07mode_kv\x18\x02 \x01(\x08\x12\x15\n\x02kv\x18\x03 \x01(\x0b\x32\t.KeyValue\x12\x14\n\x05nodes\x18\x04 \x03(\x0b\x32\x05.Node2\x8b\x01\n\x07KadImpl\x12\x1f\n\x08\x46indNode\x12\x06.IDKey\x1a\t.NodeList\"\x00\x12\'\n\tFindValue\x12\x06.IDKey\x1a\x10.KV_Node_Wrapper\"\x00\x12\x1c\n\x05Store\x12\t.KeyValue\x1a\x06.IDKey\"\x00\x12\x18\n\x04Quit\x12\x06.IDKey\x1a\x06.IDKey\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'csci4220_hw4_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NODE']._serialized_start=22
  _globals['_NODE']._serialized_end=71
  _globals['_NODELIST']._serialized_start=73
  _globals['_NODELIST']._serialized_end=137
  _globals['_IDKEY']._serialized_start=139
  _globals['_IDKEY']._serialized_end=182
  _globals['_KEYVALUE']._serialized_start=184
  _globals['_KEYVALUE']._serialized_end=243
  _globals['_KV_NODE_WRAPPER']._serialized_start=245
  _globals['_KV_NODE_WRAPPER']._serialized_end=356
  _globals['_KADIMPL']._serialized_start=359
  _globals['_KADIMPL']._serialized_end=498
# @@protoc_insertion_point(module_scope)
