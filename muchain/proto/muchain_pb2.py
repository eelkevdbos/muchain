# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: muchain/proto/muchain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='muchain/proto/muchain.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bmuchain/proto/muchain.proto\x1a\x1bgoogle/protobuf/empty.proto\"X\n\x05\x42lock\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\r\n\x05nonce\x18\x03 \x01(\x05\x12\x15\n\rprevious_hash\x18\x04 \x01(\t\x12\x0c\n\x04hash\x18\x05 \x01(\t\"%\n\x08Response\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"!\n\x11\x42lockHashResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t2\xba\x01\n\x07MuChain\x12\x1b\n\tMineBlock\x12\x06.Block\x1a\x06.Block\x12+\n\x16ReceivePropagatedBlock\x12\x06.Block\x1a\t.Response\x12-\n\x0bLatestBlock\x12\x16.google.protobuf.Empty\x1a\x06.Block\x12\x36\n\x04Ping\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Block.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='Block.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='Block.nonce', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='Block.previous_hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Block.hash', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=148,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='Response.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=187,
)


_BLOCKHASHRESPONSE = _descriptor.Descriptor(
  name='BlockHashResponse',
  full_name='BlockHashResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='BlockHashResponse.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=222,
)

DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['BlockHashResponse'] = _BLOCKHASHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'muchain.proto.muchain_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  ))
_sym_db.RegisterMessage(Block)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'muchain.proto.muchain_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)

BlockHashResponse = _reflection.GeneratedProtocolMessageType('BlockHashResponse', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHASHRESPONSE,
  __module__ = 'muchain.proto.muchain_pb2'
  # @@protoc_insertion_point(class_scope:BlockHashResponse)
  ))
_sym_db.RegisterMessage(BlockHashResponse)



_MUCHAIN = _descriptor.ServiceDescriptor(
  name='MuChain',
  full_name='MuChain',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=225,
  serialized_end=411,
  methods=[
  _descriptor.MethodDescriptor(
    name='MineBlock',
    full_name='MuChain.MineBlock',
    index=0,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_BLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReceivePropagatedBlock',
    full_name='MuChain.ReceivePropagatedBlock',
    index=1,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LatestBlock',
    full_name='MuChain.LatestBlock',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='MuChain.Ping',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MUCHAIN)

DESCRIPTOR.services_by_name['MuChain'] = _MUCHAIN

# @@protoc_insertion_point(module_scope)