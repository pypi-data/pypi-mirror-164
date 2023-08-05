# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: informaticsmatters/protobuf/datamanager/pod_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='informaticsmatters/protobuf/datamanager/pod_message.proto',
  package='informaticsmatters.protobuf.datamanager',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9informaticsmatters/protobuf/datamanager/pod_message.proto\x12\'informaticsmatters.protobuf.datamanager\"\xd4\x01\n\nPodMessage\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x10\n\x08pod_name\x18\x02 \x01(\t\x12\x0f\n\x07task_id\x18\x03 \x01(\t\x12\x0f\n\x07purpose\x18\x04 \x01(\r\x12\r\n\x05phase\x18\x05 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x06 \x01(\t\x12\x18\n\x10\x66inish_timestamp\x18\x07 \x01(\t\x12\x15\n\rhas_exit_code\x18\x10 \x01(\x08\x12\x11\n\texit_code\x18\x11 \x01(\r\x12\x13\n\x0binstance_id\x18\x12 \x01(\tb\x06proto3'
)




_PODMESSAGE = _descriptor.Descriptor(
  name='PodMessage',
  full_name='informaticsmatters.protobuf.datamanager.PodMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='informaticsmatters.protobuf.datamanager.PodMessage.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pod_name', full_name='informaticsmatters.protobuf.datamanager.PodMessage.pod_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='informaticsmatters.protobuf.datamanager.PodMessage.task_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='purpose', full_name='informaticsmatters.protobuf.datamanager.PodMessage.purpose', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phase', full_name='informaticsmatters.protobuf.datamanager.PodMessage.phase', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='informaticsmatters.protobuf.datamanager.PodMessage.start_timestamp', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finish_timestamp', full_name='informaticsmatters.protobuf.datamanager.PodMessage.finish_timestamp', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_exit_code', full_name='informaticsmatters.protobuf.datamanager.PodMessage.has_exit_code', index=7,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='informaticsmatters.protobuf.datamanager.PodMessage.exit_code', index=8,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='informaticsmatters.protobuf.datamanager.PodMessage.instance_id', index=9,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=103,
  serialized_end=315,
)

DESCRIPTOR.message_types_by_name['PodMessage'] = _PODMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PodMessage = _reflection.GeneratedProtocolMessageType('PodMessage', (_message.Message,), {
  'DESCRIPTOR' : _PODMESSAGE,
  '__module__' : 'informaticsmatters.protobuf.datamanager.pod_message_pb2'
  # @@protoc_insertion_point(class_scope:informaticsmatters.protobuf.datamanager.PodMessage)
  })
_sym_db.RegisterMessage(PodMessage)


# @@protoc_insertion_point(module_scope)
