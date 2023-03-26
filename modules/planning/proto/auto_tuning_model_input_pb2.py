# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/proto/auto_tuning_model_input.proto

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
  name='modules/planning/proto/auto_tuning_model_input.proto',
  package='apollo.planning.autotuning',
  syntax='proto2',
  serialized_pb=_b('\n4modules/planning/proto/auto_tuning_model_input.proto\x12\x1a\x61pollo.planning.autotuning\"\xf9\x04\n\x14PathPointwiseFeature\x12\t\n\x01l\x18\x01 \x01(\x01\x12\n\n\x02\x64l\x18\x02 \x01(\x01\x12\x0b\n\x03\x64\x64l\x18\x03 \x01(\x01\x12\r\n\x05kappa\x18\x04 \x01(\x01\x12W\n\robstacle_info\x18\x05 \x03(\x0b\x32@.apollo.planning.autotuning.PathPointwiseFeature.ObstacleFeature\x12`\n\x12left_bound_feature\x18\x06 \x01(\x0b\x32\x44.apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature\x12\x61\n\x13right_bound_feature\x18\x07 \x01(\x0b\x32\x44.apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature\x1a+\n\x0fObstacleFeature\x12\x18\n\x10lateral_distance\x18\x01 \x01(\x01\x1a\xe2\x01\n\x13\x42oundRelatedFeature\x12\x16\n\x0e\x62ound_distance\x18\x01 \x01(\x01\x12l\n\x0f\x63rossable_level\x18\x02 \x01(\x0e\x32S.apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature.CrossableLevel\"E\n\x0e\x43rossableLevel\x12\x0e\n\nCROSS_FREE\x10\x00\x12\x0e\n\nCROSS_ABLE\x10\x01\x12\x13\n\x0f\x43ROSS_FORBIDDEN\x10\x02\"\x87\x08\n\x15SpeedPointwiseFeature\x12\x0c\n\x01s\x18\x01 \x01(\x01:\x01\x30\x12\x0c\n\x01t\x18\x02 \x01(\x01:\x01\x30\x12\x0c\n\x01v\x18\x03 \x01(\x01:\x01\x30\x12\x16\n\x0bspeed_limit\x18\x04 \x01(\x01:\x01\x30\x12\x0e\n\x03\x61\x63\x63\x18\x05 \x01(\x01:\x01\x30\x12\x0f\n\x04jerk\x18\x06 \x01(\x01:\x01\x30\x12]\n\x12\x66ollow_obs_feature\x18\x07 \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12_\n\x14overtake_obs_feature\x18\x08 \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\\\n\x11nudge_obs_feature\x18\t \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12[\n\x10stop_obs_feature\x18\n \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\x1a\n\x0f\x63ollision_times\x18\x0b \x01(\x05:\x01\x30\x12^\n\x13virtual_obs_feature\x18\x0c \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\x16\n\x0blateral_acc\x18\r \x01(\x01:\x01\x30\x12\x1d\n\x12path_curvature_abs\x18\x0e \x01(\x01:\x01\x30\x12\x65\n\x1asidepass_front_obs_feature\x18\x0f \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x12\x64\n\x19sidepass_rear_obs_feature\x18\x10 \x03(\x0b\x32\x41.apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature\x1a\x8f\x01\n\x0fObstacleFeature\x12\x1d\n\x15longitudinal_distance\x18\x01 \x01(\x01\x12\x16\n\x0eobstacle_speed\x18\x02 \x01(\x01\x12\x1c\n\x10lateral_distance\x18\x03 \x01(\x01:\x02\x31\x30\x12\x13\n\x0bprobability\x18\x04 \x01(\x01\x12\x12\n\nrelative_v\x18\x05 \x01(\x01\"\xba\x01\n\x1aTrajectoryPointwiseFeature\x12L\n\x12path_input_feature\x18\x01 \x01(\x0b\x32\x30.apollo.planning.autotuning.PathPointwiseFeature\x12N\n\x13speed_input_feature\x18\x02 \x01(\x0b\x32\x31.apollo.planning.autotuning.SpeedPointwiseFeature\"b\n\x11TrajectoryFeature\x12M\n\rpoint_feature\x18\x01 \x03(\x0b\x32\x36.apollo.planning.autotuning.TrajectoryPointwiseFeature')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL = _descriptor.EnumDescriptor(
  name='CrossableLevel',
  full_name='apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature.CrossableLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CROSS_FREE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSS_ABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSS_FORBIDDEN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=649,
  serialized_end=718,
)
_sym_db.RegisterEnumDescriptor(_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL)


_PATHPOINTWISEFEATURE_OBSTACLEFEATURE = _descriptor.Descriptor(
  name='ObstacleFeature',
  full_name='apollo.planning.autotuning.PathPointwiseFeature.ObstacleFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lateral_distance', full_name='apollo.planning.autotuning.PathPointwiseFeature.ObstacleFeature.lateral_distance', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=446,
  serialized_end=489,
)

_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE = _descriptor.Descriptor(
  name='BoundRelatedFeature',
  full_name='apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bound_distance', full_name='apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature.bound_distance', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crossable_level', full_name='apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature.crossable_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=718,
)

_PATHPOINTWISEFEATURE = _descriptor.Descriptor(
  name='PathPointwiseFeature',
  full_name='apollo.planning.autotuning.PathPointwiseFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='l', full_name='apollo.planning.autotuning.PathPointwiseFeature.l', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl', full_name='apollo.planning.autotuning.PathPointwiseFeature.dl', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ddl', full_name='apollo.planning.autotuning.PathPointwiseFeature.ddl', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kappa', full_name='apollo.planning.autotuning.PathPointwiseFeature.kappa', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obstacle_info', full_name='apollo.planning.autotuning.PathPointwiseFeature.obstacle_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_bound_feature', full_name='apollo.planning.autotuning.PathPointwiseFeature.left_bound_feature', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_bound_feature', full_name='apollo.planning.autotuning.PathPointwiseFeature.right_bound_feature', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PATHPOINTWISEFEATURE_OBSTACLEFEATURE, _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=718,
)


_SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE = _descriptor.Descriptor(
  name='ObstacleFeature',
  full_name='apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='longitudinal_distance', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature.longitudinal_distance', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='obstacle_speed', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature.obstacle_speed', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_distance', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature.lateral_distance', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(10),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probability', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature.probability', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_v', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature.relative_v', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1609,
  serialized_end=1752,
)

_SPEEDPOINTWISEFEATURE = _descriptor.Descriptor(
  name='SpeedPointwiseFeature',
  full_name='apollo.planning.autotuning.SpeedPointwiseFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.s', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.t', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.v', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.speed_limit', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acc', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.acc', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jerk', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.jerk', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='follow_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.follow_obs_feature', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overtake_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.overtake_obs_feature', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nudge_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.nudge_obs_feature', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.stop_obs_feature', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_times', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.collision_times', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='virtual_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.virtual_obs_feature', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lateral_acc', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.lateral_acc', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_curvature_abs', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.path_curvature_abs', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sidepass_front_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.sidepass_front_obs_feature', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sidepass_rear_obs_feature', full_name='apollo.planning.autotuning.SpeedPointwiseFeature.sidepass_rear_obs_feature', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=1752,
)


_TRAJECTORYPOINTWISEFEATURE = _descriptor.Descriptor(
  name='TrajectoryPointwiseFeature',
  full_name='apollo.planning.autotuning.TrajectoryPointwiseFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path_input_feature', full_name='apollo.planning.autotuning.TrajectoryPointwiseFeature.path_input_feature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_input_feature', full_name='apollo.planning.autotuning.TrajectoryPointwiseFeature.speed_input_feature', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1755,
  serialized_end=1941,
)


_TRAJECTORYFEATURE = _descriptor.Descriptor(
  name='TrajectoryFeature',
  full_name='apollo.planning.autotuning.TrajectoryFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_feature', full_name='apollo.planning.autotuning.TrajectoryFeature.point_feature', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1943,
  serialized_end=2041,
)

_PATHPOINTWISEFEATURE_OBSTACLEFEATURE.containing_type = _PATHPOINTWISEFEATURE
_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE.fields_by_name['crossable_level'].enum_type = _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL
_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE.containing_type = _PATHPOINTWISEFEATURE
_PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE_CROSSABLELEVEL.containing_type = _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE
_PATHPOINTWISEFEATURE.fields_by_name['obstacle_info'].message_type = _PATHPOINTWISEFEATURE_OBSTACLEFEATURE
_PATHPOINTWISEFEATURE.fields_by_name['left_bound_feature'].message_type = _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE
_PATHPOINTWISEFEATURE.fields_by_name['right_bound_feature'].message_type = _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE
_SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE.containing_type = _SPEEDPOINTWISEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['follow_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['overtake_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['nudge_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['stop_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['virtual_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['sidepass_front_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_SPEEDPOINTWISEFEATURE.fields_by_name['sidepass_rear_obs_feature'].message_type = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE
_TRAJECTORYPOINTWISEFEATURE.fields_by_name['path_input_feature'].message_type = _PATHPOINTWISEFEATURE
_TRAJECTORYPOINTWISEFEATURE.fields_by_name['speed_input_feature'].message_type = _SPEEDPOINTWISEFEATURE
_TRAJECTORYFEATURE.fields_by_name['point_feature'].message_type = _TRAJECTORYPOINTWISEFEATURE
DESCRIPTOR.message_types_by_name['PathPointwiseFeature'] = _PATHPOINTWISEFEATURE
DESCRIPTOR.message_types_by_name['SpeedPointwiseFeature'] = _SPEEDPOINTWISEFEATURE
DESCRIPTOR.message_types_by_name['TrajectoryPointwiseFeature'] = _TRAJECTORYPOINTWISEFEATURE
DESCRIPTOR.message_types_by_name['TrajectoryFeature'] = _TRAJECTORYFEATURE

PathPointwiseFeature = _reflection.GeneratedProtocolMessageType('PathPointwiseFeature', (_message.Message,), dict(

  ObstacleFeature = _reflection.GeneratedProtocolMessageType('ObstacleFeature', (_message.Message,), dict(
    DESCRIPTOR = _PATHPOINTWISEFEATURE_OBSTACLEFEATURE,
    __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.PathPointwiseFeature.ObstacleFeature)
    ))
  ,

  BoundRelatedFeature = _reflection.GeneratedProtocolMessageType('BoundRelatedFeature', (_message.Message,), dict(
    DESCRIPTOR = _PATHPOINTWISEFEATURE_BOUNDRELATEDFEATURE,
    __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.PathPointwiseFeature.BoundRelatedFeature)
    ))
  ,
  DESCRIPTOR = _PATHPOINTWISEFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.PathPointwiseFeature)
  ))
_sym_db.RegisterMessage(PathPointwiseFeature)
_sym_db.RegisterMessage(PathPointwiseFeature.ObstacleFeature)
_sym_db.RegisterMessage(PathPointwiseFeature.BoundRelatedFeature)

SpeedPointwiseFeature = _reflection.GeneratedProtocolMessageType('SpeedPointwiseFeature', (_message.Message,), dict(

  ObstacleFeature = _reflection.GeneratedProtocolMessageType('ObstacleFeature', (_message.Message,), dict(
    DESCRIPTOR = _SPEEDPOINTWISEFEATURE_OBSTACLEFEATURE,
    __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.SpeedPointwiseFeature.ObstacleFeature)
    ))
  ,
  DESCRIPTOR = _SPEEDPOINTWISEFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.SpeedPointwiseFeature)
  ))
_sym_db.RegisterMessage(SpeedPointwiseFeature)
_sym_db.RegisterMessage(SpeedPointwiseFeature.ObstacleFeature)

TrajectoryPointwiseFeature = _reflection.GeneratedProtocolMessageType('TrajectoryPointwiseFeature', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYPOINTWISEFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.TrajectoryPointwiseFeature)
  ))
_sym_db.RegisterMessage(TrajectoryPointwiseFeature)

TrajectoryFeature = _reflection.GeneratedProtocolMessageType('TrajectoryFeature', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_model_input_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.TrajectoryFeature)
  ))
_sym_db.RegisterMessage(TrajectoryFeature)


# @@protoc_insertion_point(module_scope)
