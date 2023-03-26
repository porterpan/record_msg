# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/camera_detection_config.proto

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
  name='modules/perception/pipeline/proto/camera_detection_config.proto',
  package='apollo.perception.pipeline',
  syntax='proto2',
  serialized_pb=_b('\n?modules/perception/pipeline/proto/camera_detection_config.proto\x12\x1a\x61pollo.perception.pipeline\"B\n\x0bPluginParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08root_dir\x18\x02 \x01(\t\x12\x13\n\x0b\x63onfig_file\x18\x03 \x01(\t\"T\n\x13ObjectTemplateParam\x12=\n\x0cplugin_param\x18\x01 \x01(\x0b\x32\'.apollo.perception.pipeline.PluginParam\"\xd0\x01\n\nDebugParam\x12\x19\n\x11\x64\x65tection_out_dir\x18\x01 \x01(\t\x12!\n\x19tracked_detection_out_dir\x18\x02 \x01(\t\x12\x16\n\x0etrack_out_file\x18\x03 \x01(\t\x12\x1a\n\x12\x64\x65tect_feature_dir\x18\x04 \x01(\t\x12\x14\n\x0clane_out_dir\x18\x05 \x01(\t\x12\x1d\n\x15\x63\x61mera2world_out_file\x18\x06 \x01(\t\x12\x1b\n\x13\x63\x61libration_out_dir\x18\x07 \x01(\t\"\xc9\x01\n\x15\x43\x61meraDetectionConfig\x12\x0e\n\x06gpu_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61mera_name\x18\x02 \x01(\t\x12;\n\x0b\x64\x65\x62ug_param\x18\x03 \x01(\x0b\x32&.apollo.perception.pipeline.DebugParam\x12N\n\x15object_template_param\x18\x04 \x01(\x0b\x32/.apollo.perception.pipeline.ObjectTemplateParam')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLUGINPARAM = _descriptor.Descriptor(
  name='PluginParam',
  full_name='apollo.perception.pipeline.PluginParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.perception.pipeline.PluginParam.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_dir', full_name='apollo.perception.pipeline.PluginParam.root_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_file', full_name='apollo.perception.pipeline.PluginParam.config_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=95,
  serialized_end=161,
)


_OBJECTTEMPLATEPARAM = _descriptor.Descriptor(
  name='ObjectTemplateParam',
  full_name='apollo.perception.pipeline.ObjectTemplateParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_param', full_name='apollo.perception.pipeline.ObjectTemplateParam.plugin_param', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=163,
  serialized_end=247,
)


_DEBUGPARAM = _descriptor.Descriptor(
  name='DebugParam',
  full_name='apollo.perception.pipeline.DebugParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detection_out_dir', full_name='apollo.perception.pipeline.DebugParam.detection_out_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracked_detection_out_dir', full_name='apollo.perception.pipeline.DebugParam.tracked_detection_out_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track_out_file', full_name='apollo.perception.pipeline.DebugParam.track_out_file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detect_feature_dir', full_name='apollo.perception.pipeline.DebugParam.detect_feature_dir', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane_out_dir', full_name='apollo.perception.pipeline.DebugParam.lane_out_dir', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera2world_out_file', full_name='apollo.perception.pipeline.DebugParam.camera2world_out_file', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calibration_out_dir', full_name='apollo.perception.pipeline.DebugParam.calibration_out_dir', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=250,
  serialized_end=458,
)


_CAMERADETECTIONCONFIG = _descriptor.Descriptor(
  name='CameraDetectionConfig',
  full_name='apollo.perception.pipeline.CameraDetectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpu_id', full_name='apollo.perception.pipeline.CameraDetectionConfig.gpu_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera_name', full_name='apollo.perception.pipeline.CameraDetectionConfig.camera_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug_param', full_name='apollo.perception.pipeline.CameraDetectionConfig.debug_param', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_template_param', full_name='apollo.perception.pipeline.CameraDetectionConfig.object_template_param', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=461,
  serialized_end=662,
)

_OBJECTTEMPLATEPARAM.fields_by_name['plugin_param'].message_type = _PLUGINPARAM
_CAMERADETECTIONCONFIG.fields_by_name['debug_param'].message_type = _DEBUGPARAM
_CAMERADETECTIONCONFIG.fields_by_name['object_template_param'].message_type = _OBJECTTEMPLATEPARAM
DESCRIPTOR.message_types_by_name['PluginParam'] = _PLUGINPARAM
DESCRIPTOR.message_types_by_name['ObjectTemplateParam'] = _OBJECTTEMPLATEPARAM
DESCRIPTOR.message_types_by_name['DebugParam'] = _DEBUGPARAM
DESCRIPTOR.message_types_by_name['CameraDetectionConfig'] = _CAMERADETECTIONCONFIG

PluginParam = _reflection.GeneratedProtocolMessageType('PluginParam', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINPARAM,
  __module__ = 'modules.perception.pipeline.proto.camera_detection_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.PluginParam)
  ))
_sym_db.RegisterMessage(PluginParam)

ObjectTemplateParam = _reflection.GeneratedProtocolMessageType('ObjectTemplateParam', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTTEMPLATEPARAM,
  __module__ = 'modules.perception.pipeline.proto.camera_detection_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.ObjectTemplateParam)
  ))
_sym_db.RegisterMessage(ObjectTemplateParam)

DebugParam = _reflection.GeneratedProtocolMessageType('DebugParam', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGPARAM,
  __module__ = 'modules.perception.pipeline.proto.camera_detection_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.DebugParam)
  ))
_sym_db.RegisterMessage(DebugParam)

CameraDetectionConfig = _reflection.GeneratedProtocolMessageType('CameraDetectionConfig', (_message.Message,), dict(
  DESCRIPTOR = _CAMERADETECTIONCONFIG,
  __module__ = 'modules.perception.pipeline.proto.camera_detection_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.CameraDetectionConfig)
  ))
_sym_db.RegisterMessage(CameraDetectionConfig)


# @@protoc_insertion_point(module_scope)
