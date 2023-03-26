# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/stage/detection.proto

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
  name='modules/perception/pipeline/proto/stage/detection.proto',
  package='apollo.perception.camera',
  syntax='proto2',
  serialized_pb=_b('\n7modules/perception/pipeline/proto/stage/detection.proto\x12\x18\x61pollo.perception.camera\"\xb7\x04\n\x1bTrafficLightDetectionConfig\x12\x1a\n\rmin_crop_size\x18\x01 \x01(\x05:\x03\x32\x37\x30\x12\x16\n\x0b\x63rop_method\x18\x02 \x01(\x05:\x01\x30\x12\x12\n\x06mean_b\x18\x03 \x01(\x02:\x02\x39\x35\x12\x12\n\x06mean_g\x18\x04 \x01(\x02:\x02\x39\x39\x12\x12\n\x06mean_r\x18\x05 \x01(\x02:\x02\x39\x36\x12\x14\n\x06is_bgr\x18\x06 \x01(\x08:\x04true\x12\x17\n\ncrop_scale\x18\x07 \x01(\x02:\x03\x32.5\x12\x17\n\x0finput_blob_name\x18\x08 \x01(\t\x12\x1a\n\x12im_param_blob_name\x18\t \x01(\t\x12\x18\n\x10output_blob_name\x18\n \x01(\t\x12\x19\n\nmodel_name\x18\x0b \x01(\t:\x05RTNet\x12\x19\n\nmodel_type\x18\x0c \x01(\t:\x05RTNet\x12\x1c\n\nproto_file\x18\r \x01(\t:\x08\x63\x61\x66\x66\x65.pt\x12 \n\x0bweight_file\x18\x0e \x01(\t:\x0b\x63\x61\x66\x66\x65.model\x12\x19\n\x0emax_batch_size\x18\x0f \x01(\x05:\x01\x31\x12\x85\x01\n traffic_light_detection_root_dir\x18\x10 \x01(\t:[/apollo/modules/perception/production/data/perception/camera/models/traffic_light_detection\x12\x11\n\x06gpu_id\x18\x11 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRAFFICLIGHTDETECTIONCONFIG = _descriptor.Descriptor(
  name='TrafficLightDetectionConfig',
  full_name='apollo.perception.camera.TrafficLightDetectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_crop_size', full_name='apollo.perception.camera.TrafficLightDetectionConfig.min_crop_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=270,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_method', full_name='apollo.perception.camera.TrafficLightDetectionConfig.crop_method', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_b', full_name='apollo.perception.camera.TrafficLightDetectionConfig.mean_b', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(95),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_g', full_name='apollo.perception.camera.TrafficLightDetectionConfig.mean_g', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(99),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_r', full_name='apollo.perception.camera.TrafficLightDetectionConfig.mean_r', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(96),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_bgr', full_name='apollo.perception.camera.TrafficLightDetectionConfig.is_bgr', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crop_scale', full_name='apollo.perception.camera.TrafficLightDetectionConfig.crop_scale', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(2.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_blob_name', full_name='apollo.perception.camera.TrafficLightDetectionConfig.input_blob_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='im_param_blob_name', full_name='apollo.perception.camera.TrafficLightDetectionConfig.im_param_blob_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_blob_name', full_name='apollo.perception.camera.TrafficLightDetectionConfig.output_blob_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='apollo.perception.camera.TrafficLightDetectionConfig.model_name', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("RTNet").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_type', full_name='apollo.perception.camera.TrafficLightDetectionConfig.model_type', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("RTNet").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto_file', full_name='apollo.perception.camera.TrafficLightDetectionConfig.proto_file', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("caffe.pt").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_file', full_name='apollo.perception.camera.TrafficLightDetectionConfig.weight_file', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("caffe.model").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_batch_size', full_name='apollo.perception.camera.TrafficLightDetectionConfig.max_batch_size', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_light_detection_root_dir', full_name='apollo.perception.camera.TrafficLightDetectionConfig.traffic_light_detection_root_dir', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("/apollo/modules/perception/production/data/perception/camera/models/traffic_light_detection").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu_id', full_name='apollo.perception.camera.TrafficLightDetectionConfig.gpu_id', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=86,
  serialized_end=653,
)

DESCRIPTOR.message_types_by_name['TrafficLightDetectionConfig'] = _TRAFFICLIGHTDETECTIONCONFIG

TrafficLightDetectionConfig = _reflection.GeneratedProtocolMessageType('TrafficLightDetectionConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHTDETECTIONCONFIG,
  __module__ = 'modules.perception.pipeline.proto.stage.detection_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.TrafficLightDetectionConfig)
  ))
_sym_db.RegisterMessage(TrafficLightDetectionConfig)


# @@protoc_insertion_point(module_scope)
