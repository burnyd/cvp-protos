# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/event.v1/services.gen.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arista.event.v1 import event_pb2 as arista_dot_event_dot_v1_dot_event__pb2
from arista.time import time_pb2 as arista_dot_time_dot_time__pb2
from arista.subscriptions import subscriptions_pb2 as arista_dot_subscriptions_dot_subscriptions__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arista/event.v1/services.gen.proto',
  package='arista.event.v1',
  syntax='proto3',
  serialized_options=b'Z&arista/resources/arista/event.v1;event',
  serialized_pb=b'\n\"arista/event.v1/services.gen.proto\x12\x0f\x61rista.event.v1\x1a\x1b\x61rista/event.v1/event.proto\x1a\x16\x61rista/time/time.proto\x1a(arista/subscriptions/subscriptions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"`\n\x0c\x45ventRequest\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.arista.event.v1.EventKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"`\n\rEventResponse\x12%\n\x05value\x18\x01 \x01(\x0b\x32\x16.arista.event.v1.Event\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"n\n\x12\x45ventStreamRequest\x12\x31\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32\x16.arista.event.v1.Event\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\x95\x01\n\x13\x45ventStreamResponse\x12%\n\x05value\x18\x01 \x01(\x0b\x32\x16.arista.event.v1.Event\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"p\n\x1c\x45ventAnnotationConfigRequest\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.arista.event.v1.EventKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x80\x01\n\x1d\x45ventAnnotationConfigResponse\x12\x35\n\x05value\x18\x01 \x01(\x0b\x32&.arista.event.v1.EventAnnotationConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8e\x01\n\"EventAnnotationConfigStreamRequest\x12\x41\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32&.arista.event.v1.EventAnnotationConfig\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\xb5\x01\n#EventAnnotationConfigStreamResponse\x12\x35\n\x05value\x18\x01 \x01(\x0b\x32&.arista.event.v1.EventAnnotationConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"X\n\x1f\x45ventAnnotationConfigSetRequest\x12\x35\n\x05value\x18\x01 \x01(\x0b\x32&.arista.event.v1.EventAnnotationConfig\"\x83\x01\n EventAnnotationConfigSetResponse\x12\x35\n\x05value\x18\x01 \x01(\x0b\x32&.arista.event.v1.EventAnnotationConfig\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"L\n\"EventAnnotationConfigDeleteRequest\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.arista.event.v1.EventKey\"w\n#EventAnnotationConfigDeleteResponse\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.arista.event.v1.EventKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\x88\x02\n\x0c\x45ventService\x12G\n\x06GetOne\x12\x1d.arista.event.v1.EventRequest\x1a\x1e.arista.event.v1.EventResponse\x12U\n\x06GetAll\x12#.arista.event.v1.EventStreamRequest\x1a$.arista.event.v1.EventStreamResponse0\x01\x12X\n\tSubscribe\x12#.arista.event.v1.EventStreamRequest\x1a$.arista.event.v1.EventStreamResponse0\x01\x32\xd9\x04\n\x1c\x45ventAnnotationConfigService\x12g\n\x06GetOne\x12-.arista.event.v1.EventAnnotationConfigRequest\x1a..arista.event.v1.EventAnnotationConfigResponse\x12u\n\x06GetAll\x12\x33.arista.event.v1.EventAnnotationConfigStreamRequest\x1a\x34.arista.event.v1.EventAnnotationConfigStreamResponse0\x01\x12x\n\tSubscribe\x12\x33.arista.event.v1.EventAnnotationConfigStreamRequest\x1a\x34.arista.event.v1.EventAnnotationConfigStreamResponse0\x01\x12j\n\x03Set\x12\x30.arista.event.v1.EventAnnotationConfigSetRequest\x1a\x31.arista.event.v1.EventAnnotationConfigSetResponse\x12s\n\x06\x44\x65lete\x12\x33.arista.event.v1.EventAnnotationConfigDeleteRequest\x1a\x34.arista.event.v1.EventAnnotationConfigDeleteResponseB(Z&arista/resources/arista/event.v1;eventb\x06proto3'
  ,
  dependencies=[arista_dot_event_dot_v1_dot_event__pb2.DESCRIPTOR,arista_dot_time_dot_time__pb2.DESCRIPTOR,arista_dot_subscriptions_dot_subscriptions__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_EVENTREQUEST = _descriptor.Descriptor(
  name='EventRequest',
  full_name='arista.event.v1.EventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arista.event.v1.EventRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventRequest.time', index=1,
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
  serialized_start=183,
  serialized_end=279,
)


_EVENTRESPONSE = _descriptor.Descriptor(
  name='EventResponse',
  full_name='arista.event.v1.EventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='arista.event.v1.EventResponse.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventResponse.time', index=1,
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
  serialized_start=281,
  serialized_end=377,
)


_EVENTSTREAMREQUEST = _descriptor.Descriptor(
  name='EventStreamRequest',
  full_name='arista.event.v1.EventStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_eq_filter', full_name='arista.event.v1.EventStreamRequest.partial_eq_filter', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventStreamRequest.time', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=379,
  serialized_end=489,
)


_EVENTSTREAMRESPONSE = _descriptor.Descriptor(
  name='EventStreamResponse',
  full_name='arista.event.v1.EventStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='arista.event.v1.EventStreamResponse.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventStreamResponse.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='arista.event.v1.EventStreamResponse.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=492,
  serialized_end=641,
)


_EVENTANNOTATIONCONFIGREQUEST = _descriptor.Descriptor(
  name='EventAnnotationConfigRequest',
  full_name='arista.event.v1.EventAnnotationConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arista.event.v1.EventAnnotationConfigRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventAnnotationConfigRequest.time', index=1,
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
  serialized_start=643,
  serialized_end=755,
)


_EVENTANNOTATIONCONFIGRESPONSE = _descriptor.Descriptor(
  name='EventAnnotationConfigResponse',
  full_name='arista.event.v1.EventAnnotationConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='arista.event.v1.EventAnnotationConfigResponse.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventAnnotationConfigResponse.time', index=1,
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
  serialized_start=758,
  serialized_end=886,
)


_EVENTANNOTATIONCONFIGSTREAMREQUEST = _descriptor.Descriptor(
  name='EventAnnotationConfigStreamRequest',
  full_name='arista.event.v1.EventAnnotationConfigStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_eq_filter', full_name='arista.event.v1.EventAnnotationConfigStreamRequest.partial_eq_filter', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventAnnotationConfigStreamRequest.time', index=1,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=889,
  serialized_end=1031,
)


_EVENTANNOTATIONCONFIGSTREAMRESPONSE = _descriptor.Descriptor(
  name='EventAnnotationConfigStreamResponse',
  full_name='arista.event.v1.EventAnnotationConfigStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='arista.event.v1.EventAnnotationConfigStreamResponse.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventAnnotationConfigStreamResponse.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='arista.event.v1.EventAnnotationConfigStreamResponse.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1034,
  serialized_end=1215,
)


_EVENTANNOTATIONCONFIGSETREQUEST = _descriptor.Descriptor(
  name='EventAnnotationConfigSetRequest',
  full_name='arista.event.v1.EventAnnotationConfigSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='arista.event.v1.EventAnnotationConfigSetRequest.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1217,
  serialized_end=1305,
)


_EVENTANNOTATIONCONFIGSETRESPONSE = _descriptor.Descriptor(
  name='EventAnnotationConfigSetResponse',
  full_name='arista.event.v1.EventAnnotationConfigSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='arista.event.v1.EventAnnotationConfigSetResponse.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventAnnotationConfigSetResponse.time', index=1,
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
  serialized_start=1308,
  serialized_end=1439,
)


_EVENTANNOTATIONCONFIGDELETEREQUEST = _descriptor.Descriptor(
  name='EventAnnotationConfigDeleteRequest',
  full_name='arista.event.v1.EventAnnotationConfigDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arista.event.v1.EventAnnotationConfigDeleteRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1441,
  serialized_end=1517,
)


_EVENTANNOTATIONCONFIGDELETERESPONSE = _descriptor.Descriptor(
  name='EventAnnotationConfigDeleteResponse',
  full_name='arista.event.v1.EventAnnotationConfigDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arista.event.v1.EventAnnotationConfigDeleteResponse.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='arista.event.v1.EventAnnotationConfigDeleteResponse.time', index=1,
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
  serialized_start=1519,
  serialized_end=1638,
)

_EVENTREQUEST.fields_by_name['key'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTKEY
_EVENTREQUEST.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTRESPONSE.fields_by_name['value'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENT
_EVENTRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTSTREAMREQUEST.fields_by_name['partial_eq_filter'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENT
_EVENTSTREAMREQUEST.fields_by_name['time'].message_type = arista_dot_time_dot_time__pb2._TIMEBOUNDS
_EVENTSTREAMRESPONSE.fields_by_name['value'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENT
_EVENTSTREAMRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTSTREAMRESPONSE.fields_by_name['type'].enum_type = arista_dot_subscriptions_dot_subscriptions__pb2._OPERATION
_EVENTANNOTATIONCONFIGREQUEST.fields_by_name['key'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTKEY
_EVENTANNOTATIONCONFIGREQUEST.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTANNOTATIONCONFIGRESPONSE.fields_by_name['value'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTANNOTATIONCONFIG
_EVENTANNOTATIONCONFIGRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTANNOTATIONCONFIGSTREAMREQUEST.fields_by_name['partial_eq_filter'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTANNOTATIONCONFIG
_EVENTANNOTATIONCONFIGSTREAMREQUEST.fields_by_name['time'].message_type = arista_dot_time_dot_time__pb2._TIMEBOUNDS
_EVENTANNOTATIONCONFIGSTREAMRESPONSE.fields_by_name['value'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTANNOTATIONCONFIG
_EVENTANNOTATIONCONFIGSTREAMRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTANNOTATIONCONFIGSTREAMRESPONSE.fields_by_name['type'].enum_type = arista_dot_subscriptions_dot_subscriptions__pb2._OPERATION
_EVENTANNOTATIONCONFIGSETREQUEST.fields_by_name['value'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTANNOTATIONCONFIG
_EVENTANNOTATIONCONFIGSETRESPONSE.fields_by_name['value'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTANNOTATIONCONFIG
_EVENTANNOTATIONCONFIGSETRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTANNOTATIONCONFIGDELETEREQUEST.fields_by_name['key'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTKEY
_EVENTANNOTATIONCONFIGDELETERESPONSE.fields_by_name['key'].message_type = arista_dot_event_dot_v1_dot_event__pb2._EVENTKEY
_EVENTANNOTATIONCONFIGDELETERESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['EventRequest'] = _EVENTREQUEST
DESCRIPTOR.message_types_by_name['EventResponse'] = _EVENTRESPONSE
DESCRIPTOR.message_types_by_name['EventStreamRequest'] = _EVENTSTREAMREQUEST
DESCRIPTOR.message_types_by_name['EventStreamResponse'] = _EVENTSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['EventAnnotationConfigRequest'] = _EVENTANNOTATIONCONFIGREQUEST
DESCRIPTOR.message_types_by_name['EventAnnotationConfigResponse'] = _EVENTANNOTATIONCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['EventAnnotationConfigStreamRequest'] = _EVENTANNOTATIONCONFIGSTREAMREQUEST
DESCRIPTOR.message_types_by_name['EventAnnotationConfigStreamResponse'] = _EVENTANNOTATIONCONFIGSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['EventAnnotationConfigSetRequest'] = _EVENTANNOTATIONCONFIGSETREQUEST
DESCRIPTOR.message_types_by_name['EventAnnotationConfigSetResponse'] = _EVENTANNOTATIONCONFIGSETRESPONSE
DESCRIPTOR.message_types_by_name['EventAnnotationConfigDeleteRequest'] = _EVENTANNOTATIONCONFIGDELETEREQUEST
DESCRIPTOR.message_types_by_name['EventAnnotationConfigDeleteResponse'] = _EVENTANNOTATIONCONFIGDELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

EventResponse = _reflection.GeneratedProtocolMessageType('EventResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRESPONSE,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventResponse)
  })
_sym_db.RegisterMessage(EventResponse)

EventStreamRequest = _reflection.GeneratedProtocolMessageType('EventStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSTREAMREQUEST,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventStreamRequest)
  })
_sym_db.RegisterMessage(EventStreamRequest)

EventStreamResponse = _reflection.GeneratedProtocolMessageType('EventStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSTREAMRESPONSE,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventStreamResponse)
  })
_sym_db.RegisterMessage(EventStreamResponse)

EventAnnotationConfigRequest = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGREQUEST,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigRequest)
  })
_sym_db.RegisterMessage(EventAnnotationConfigRequest)

EventAnnotationConfigResponse = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGRESPONSE,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigResponse)
  })
_sym_db.RegisterMessage(EventAnnotationConfigResponse)

EventAnnotationConfigStreamRequest = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGSTREAMREQUEST,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigStreamRequest)
  })
_sym_db.RegisterMessage(EventAnnotationConfigStreamRequest)

EventAnnotationConfigStreamResponse = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGSTREAMRESPONSE,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigStreamResponse)
  })
_sym_db.RegisterMessage(EventAnnotationConfigStreamResponse)

EventAnnotationConfigSetRequest = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGSETREQUEST,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigSetRequest)
  })
_sym_db.RegisterMessage(EventAnnotationConfigSetRequest)

EventAnnotationConfigSetResponse = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGSETRESPONSE,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigSetResponse)
  })
_sym_db.RegisterMessage(EventAnnotationConfigSetResponse)

EventAnnotationConfigDeleteRequest = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGDELETEREQUEST,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigDeleteRequest)
  })
_sym_db.RegisterMessage(EventAnnotationConfigDeleteRequest)

EventAnnotationConfigDeleteResponse = _reflection.GeneratedProtocolMessageType('EventAnnotationConfigDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTANNOTATIONCONFIGDELETERESPONSE,
  '__module__' : 'arista.event.v1.services.gen_pb2'
  # @@protoc_insertion_point(class_scope:arista.event.v1.EventAnnotationConfigDeleteResponse)
  })
_sym_db.RegisterMessage(EventAnnotationConfigDeleteResponse)


DESCRIPTOR._options = None

_EVENTSERVICE = _descriptor.ServiceDescriptor(
  name='EventService',
  full_name='arista.event.v1.EventService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1641,
  serialized_end=1905,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOne',
    full_name='arista.event.v1.EventService.GetOne',
    index=0,
    containing_service=None,
    input_type=_EVENTREQUEST,
    output_type=_EVENTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAll',
    full_name='arista.event.v1.EventService.GetAll',
    index=1,
    containing_service=None,
    input_type=_EVENTSTREAMREQUEST,
    output_type=_EVENTSTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='arista.event.v1.EventService.Subscribe',
    index=2,
    containing_service=None,
    input_type=_EVENTSTREAMREQUEST,
    output_type=_EVENTSTREAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSERVICE)

DESCRIPTOR.services_by_name['EventService'] = _EVENTSERVICE


_EVENTANNOTATIONCONFIGSERVICE = _descriptor.ServiceDescriptor(
  name='EventAnnotationConfigService',
  full_name='arista.event.v1.EventAnnotationConfigService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1908,
  serialized_end=2509,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOne',
    full_name='arista.event.v1.EventAnnotationConfigService.GetOne',
    index=0,
    containing_service=None,
    input_type=_EVENTANNOTATIONCONFIGREQUEST,
    output_type=_EVENTANNOTATIONCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAll',
    full_name='arista.event.v1.EventAnnotationConfigService.GetAll',
    index=1,
    containing_service=None,
    input_type=_EVENTANNOTATIONCONFIGSTREAMREQUEST,
    output_type=_EVENTANNOTATIONCONFIGSTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='arista.event.v1.EventAnnotationConfigService.Subscribe',
    index=2,
    containing_service=None,
    input_type=_EVENTANNOTATIONCONFIGSTREAMREQUEST,
    output_type=_EVENTANNOTATIONCONFIGSTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Set',
    full_name='arista.event.v1.EventAnnotationConfigService.Set',
    index=3,
    containing_service=None,
    input_type=_EVENTANNOTATIONCONFIGSETREQUEST,
    output_type=_EVENTANNOTATIONCONFIGSETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='arista.event.v1.EventAnnotationConfigService.Delete',
    index=4,
    containing_service=None,
    input_type=_EVENTANNOTATIONCONFIGDELETEREQUEST,
    output_type=_EVENTANNOTATIONCONFIGDELETERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTANNOTATIONCONFIGSERVICE)

DESCRIPTOR.services_by_name['EventAnnotationConfigService'] = _EVENTANNOTATIONCONFIGSERVICE

# @@protoc_insertion_point(module_scope)
