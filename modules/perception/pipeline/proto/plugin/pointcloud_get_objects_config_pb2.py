# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/plugin/pointcloud_get_objects_config.proto

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
  name='modules/perception/pipeline/proto/plugin/pointcloud_get_objects_config.proto',
  package='apollo.perception.lidar',
  syntax='proto2',
  serialized_pb=_b('\nLmodules/perception/pipeline/proto/plugin/pointcloud_get_objects_config.proto\x12\x17\x61pollo.perception.lidar\"\x1c\n\x1aPointcloudGetObjectsConfig')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POINTCLOUDGETOBJECTSCONFIG = _descriptor.Descriptor(
  name='PointcloudGetObjectsConfig',
  full_name='apollo.perception.lidar.PointcloudGetObjectsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=105,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['PointcloudGetObjectsConfig'] = _POINTCLOUDGETOBJECTSCONFIG

PointcloudGetObjectsConfig = _reflection.GeneratedProtocolMessageType('PointcloudGetObjectsConfig', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDGETOBJECTSCONFIG,
  __module__ = 'modules.perception.pipeline.proto.plugin.pointcloud_get_objects_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.PointcloudGetObjectsConfig)
  ))
_sym_db.RegisterMessage(PointcloudGetObjectsConfig)


# @@protoc_insertion_point(module_scope)
