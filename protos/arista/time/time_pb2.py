# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/time/time.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arista/time/time.proto',
  package='arista.time',
  syntax='proto3',
  serialized_options=b'Z\034arista/resources/arista/time',
  serialized_pb=b'\n\x16\x61rista/time/time.proto\x12\x0b\x61rista.time\x1a\x1fgoogle/protobuf/timestamp.proto\"`\n\nTimeBounds\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1eZ\x1c\x61rista/resources/arista/timeb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TIMEBOUNDS = _descriptor.Descriptor(
  name='TimeBounds',
  full_name='arista.time.TimeBounds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='arista.time.TimeBounds.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='arista.time.TimeBounds.end', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=72,
  serialized_end=168,
)

_TIMEBOUNDS.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEBOUNDS.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['TimeBounds'] = _TIMEBOUNDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeBounds = _reflection.GeneratedProtocolMessageType('TimeBounds', (_message.Message,), {
  'DESCRIPTOR' : _TIMEBOUNDS,
  '__module__' : 'arista.time.time_pb2'
  # @@protoc_insertion_point(class_scope:arista.time.TimeBounds)
  })
_sym_db.RegisterMessage(TimeBounds)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
