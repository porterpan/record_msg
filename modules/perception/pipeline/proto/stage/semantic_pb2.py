# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/stage/semantic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/pipeline/proto/stage/semantic.proto',
  package='apollo.perception.camera',
  syntax='proto2',
  serialized_pb=_b('\n6modules/perception/pipeline/proto/stage/semantic.proto\x12\x18\x61pollo.perception.camera\"\x89\x02\n\x15SemanticReviserConfig\x12\x1f\n\x12revise_time_second\x18\x01 \x01(\x02:\x03\x31.5\x12#\n\x16\x62link_threshold_second\x18\x02 \x01(\x02:\x03\x30.4\x12%\n\x1ahysteretic_threshold_count\x18\x03 \x01(\x05:\x01\x32\x12\x82\x01\n\x1ftraffic_light_semantic_root_dir\x18\x04 \x01(\t:Y/apollo/modules/perception/production/data/perception/camera/models/traffic_light_tracker')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEMANTICREVISERCONFIG = _descriptor.Descriptor(
  name='SemanticReviserConfig',
  full_name='apollo.perception.camera.SemanticReviserConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='revise_time_second', full_name='apollo.perception.camera.SemanticReviserConfig.revise_time_second', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blink_threshold_second', full_name='apollo.perception.camera.SemanticReviserConfig.blink_threshold_second', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.4),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hysteretic_threshold_count', full_name='apollo.perception.camera.SemanticReviserConfig.hysteretic_threshold_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_light_semantic_root_dir', full_name='apollo.perception.camera.SemanticReviserConfig.traffic_light_semantic_root_dir', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/apollo/modules/perception/production/data/perception/camera/models/traffic_light_tracker").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=350,
)

DESCRIPTOR.message_types_by_name['SemanticReviserConfig'] = _SEMANTICREVISERCONFIG

SemanticReviserConfig = _reflection.GeneratedProtocolMessageType('SemanticReviserConfig', (_message.Message,), dict(
  DESCRIPTOR = _SEMANTICREVISERCONFIG,
  __module__ = 'modules.perception.pipeline.proto.stage.semantic_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.SemanticReviserConfig)
  ))
_sym_db.RegisterMessage(SemanticReviserConfig)


# @@protoc_insertion_point(module_scope)
