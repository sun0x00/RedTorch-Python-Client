# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xyz/redtorch/pb/dep.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xyz/redtorch/pb/dep.proto',
  package='xyz.redtorch.pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19xyz/redtorch/pb/dep.proto\x12\x0fxyz.redtorch.pb\"\xc6\x01\n\x14\x44\x61taExchangeProtocol\x12\x46\n\x0b\x63ontentType\x18\x01 \x01(\x0e\x32\x31.xyz.redtorch.pb.DataExchangeProtocol.ContentType\x12\r\n\x05rpcId\x18\x02 \x01(\x07\x12\x14\n\x0c\x63ontentBytes\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x06\".\n\x0b\x43ontentType\x12\x0b\n\x07ROUTINE\x10\x00\x12\x12\n\x0e\x43OMPRESSED_LZ4\x10\x01\x62\x06proto3'
)



_DATAEXCHANGEPROTOCOL_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='xyz.redtorch.pb.DataExchangeProtocol.ContentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROUTINE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPRESSED_LZ4', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=199,
  serialized_end=245,
)
_sym_db.RegisterEnumDescriptor(_DATAEXCHANGEPROTOCOL_CONTENTTYPE)


_DATAEXCHANGEPROTOCOL = _descriptor.Descriptor(
  name='DataExchangeProtocol',
  full_name='xyz.redtorch.pb.DataExchangeProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentType', full_name='xyz.redtorch.pb.DataExchangeProtocol.contentType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rpcId', full_name='xyz.redtorch.pb.DataExchangeProtocol.rpcId', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contentBytes', full_name='xyz.redtorch.pb.DataExchangeProtocol.contentBytes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='xyz.redtorch.pb.DataExchangeProtocol.timestamp', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATAEXCHANGEPROTOCOL_CONTENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=245,
)

_DATAEXCHANGEPROTOCOL.fields_by_name['contentType'].enum_type = _DATAEXCHANGEPROTOCOL_CONTENTTYPE
_DATAEXCHANGEPROTOCOL_CONTENTTYPE.containing_type = _DATAEXCHANGEPROTOCOL
DESCRIPTOR.message_types_by_name['DataExchangeProtocol'] = _DATAEXCHANGEPROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataExchangeProtocol = _reflection.GeneratedProtocolMessageType('DataExchangeProtocol', (_message.Message,), {
  'DESCRIPTOR' : _DATAEXCHANGEPROTOCOL,
  '__module__' : 'xyz.redtorch.pb.dep_pb2'
  # @@protoc_insertion_point(class_scope:xyz.redtorch.pb.DataExchangeProtocol)
  })
_sym_db.RegisterMessage(DataExchangeProtocol)


# @@protoc_insertion_point(module_scope)
