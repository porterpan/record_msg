# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/v2x/proto/v2x_obstacles.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from modules.common_msgs.basic_msgs import error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2
from modules.common_msgs.perception_msgs import perception_obstacle_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/v2x/proto/v2x_obstacles.proto',
  package='apollo.v2x',
  syntax='proto2',
  serialized_pb=_b('\n%modules/v2x/proto/v2x_obstacles.proto\x12\napollo.v2x\x1a+modules/common_msgs/basic_msgs/header.proto\x1a/modules/common_msgs/basic_msgs/error_code.proto\x1a=modules/common_msgs/perception_msgs/perception_obstacle.proto\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"\x9f\x01\n\x0bMiniAreaMap\x12\x0f\n\x07rscu_id\x18\x01 \x01(\x0c\x12+\n\x10\x66\x65\x61ture_position\x18\x02 \x01(\x0b\x32\x11.apollo.v2x.Point\x12)\n\x0estart_position\x18\x03 \x01(\x0b\x32\x11.apollo.v2x.Point\x12\'\n\x0c\x65nd_position\x18\x04 \x01(\x0b\x32\x11.apollo.v2x.Point\"E\n\x13\x41\x62normalInformation\x12\x15\n\raverage_speed\x18\x01 \x01(\x01\x12\x17\n\x0fvehicle_density\x18\x02 \x01(\x01\"\xfc\x02\n\x0eV2XInformation\x12\x34\n\x08v2x_type\x18\x01 \x03(\x0e\x32\".apollo.v2x.V2XInformation.V2XType\x12.\n\x13traffic_event_start\x18\x03 \x01(\x0b\x32\x11.apollo.v2x.Point\x12\x34\n\x19traffic_event_start_error\x18\x04 \x01(\x0b\x32\x11.apollo.v2x.Point\x12,\n\x11traffic_event_end\x18\x05 \x01(\x0b\x32\x11.apollo.v2x.Point\x12\x32\n\x17traffic_event_end_error\x18\x06 \x01(\x0b\x32\x11.apollo.v2x.Point\x12\x36\n\rabnormal_info\x18\x07 \x01(\x0b\x32\x1f.apollo.v2x.AbnormalInformation\"4\n\x07V2XType\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bZOMBIES_CAR\x10\x01\x12\x0e\n\nBLIND_ZONE\x10\x02\"\x7f\n\x0bV2XObstacle\x12\x42\n\x13perception_obstacle\x18\x01 \x01(\x0b\x32%.apollo.perception.PerceptionObstacle\x12,\n\x08v2x_info\x18\x02 \x01(\x0b\x32\x1a.apollo.v2x.V2XInformation\"\xd7\x01\n\x0cV2XObstacles\x12-\n\x0cv2x_obstacle\x18\x01 \x03(\x0b\x32\x17.apollo.v2x.V2XObstacle\x12)\n\x08\x61rea_map\x18\x02 \x01(\x0b\x32\x17.apollo.v2x.MiniAreaMap\x12\x14\n\x0ctraffic_flow\x18\x03 \x01(\x01\x12%\n\x06header\x18\x04 \x01(\x0b\x32\x15.apollo.common.Header\x12\x30\n\nerror_code\x18\x05 \x01(\x0e\x32\x18.apollo.common.ErrorCode:\x02OK')
  ,
  dependencies=[modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2.DESCRIPTOR,modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2.DESCRIPTOR,modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_V2XINFORMATION_V2XTYPE = _descriptor.EnumDescriptor(
  name='V2XType',
  full_name='apollo.v2x.V2XInformation.V2XType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZOMBIES_CAR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLIND_ZONE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=814,
  serialized_end=866,
)
_sym_db.RegisterEnumDescriptor(_V2XINFORMATION_V2XTYPE)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='apollo.v2x.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='apollo.v2x.Point.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='apollo.v2x.Point.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='apollo.v2x.Point.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=210,
  serialized_end=250,
)


_MINIAREAMAP = _descriptor.Descriptor(
  name='MiniAreaMap',
  full_name='apollo.v2x.MiniAreaMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rscu_id', full_name='apollo.v2x.MiniAreaMap.rscu_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_position', full_name='apollo.v2x.MiniAreaMap.feature_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_position', full_name='apollo.v2x.MiniAreaMap.start_position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_position', full_name='apollo.v2x.MiniAreaMap.end_position', index=3,
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
  serialized_start=253,
  serialized_end=412,
)


_ABNORMALINFORMATION = _descriptor.Descriptor(
  name='AbnormalInformation',
  full_name='apollo.v2x.AbnormalInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='average_speed', full_name='apollo.v2x.AbnormalInformation.average_speed', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle_density', full_name='apollo.v2x.AbnormalInformation.vehicle_density', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=414,
  serialized_end=483,
)


_V2XINFORMATION = _descriptor.Descriptor(
  name='V2XInformation',
  full_name='apollo.v2x.V2XInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v2x_type', full_name='apollo.v2x.V2XInformation.v2x_type', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_event_start', full_name='apollo.v2x.V2XInformation.traffic_event_start', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_event_start_error', full_name='apollo.v2x.V2XInformation.traffic_event_start_error', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_event_end', full_name='apollo.v2x.V2XInformation.traffic_event_end', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_event_end_error', full_name='apollo.v2x.V2XInformation.traffic_event_end_error', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='abnormal_info', full_name='apollo.v2x.V2XInformation.abnormal_info', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _V2XINFORMATION_V2XTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=866,
)


_V2XOBSTACLE = _descriptor.Descriptor(
  name='V2XObstacle',
  full_name='apollo.v2x.V2XObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='perception_obstacle', full_name='apollo.v2x.V2XObstacle.perception_obstacle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v2x_info', full_name='apollo.v2x.V2XObstacle.v2x_info', index=1,
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
  serialized_start=868,
  serialized_end=995,
)


_V2XOBSTACLES = _descriptor.Descriptor(
  name='V2XObstacles',
  full_name='apollo.v2x.V2XObstacles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v2x_obstacle', full_name='apollo.v2x.V2XObstacles.v2x_obstacle', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_map', full_name='apollo.v2x.V2XObstacles.area_map', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_flow', full_name='apollo.v2x.V2XObstacles.traffic_flow', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.v2x.V2XObstacles.header', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='apollo.v2x.V2XObstacles.error_code', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=998,
  serialized_end=1213,
)

_MINIAREAMAP.fields_by_name['feature_position'].message_type = _POINT
_MINIAREAMAP.fields_by_name['start_position'].message_type = _POINT
_MINIAREAMAP.fields_by_name['end_position'].message_type = _POINT
_V2XINFORMATION.fields_by_name['v2x_type'].enum_type = _V2XINFORMATION_V2XTYPE
_V2XINFORMATION.fields_by_name['traffic_event_start'].message_type = _POINT
_V2XINFORMATION.fields_by_name['traffic_event_start_error'].message_type = _POINT
_V2XINFORMATION.fields_by_name['traffic_event_end'].message_type = _POINT
_V2XINFORMATION.fields_by_name['traffic_event_end_error'].message_type = _POINT
_V2XINFORMATION.fields_by_name['abnormal_info'].message_type = _ABNORMALINFORMATION
_V2XINFORMATION_V2XTYPE.containing_type = _V2XINFORMATION
_V2XOBSTACLE.fields_by_name['perception_obstacle'].message_type = modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2._PERCEPTIONOBSTACLE
_V2XOBSTACLE.fields_by_name['v2x_info'].message_type = _V2XINFORMATION
_V2XOBSTACLES.fields_by_name['v2x_obstacle'].message_type = _V2XOBSTACLE
_V2XOBSTACLES.fields_by_name['area_map'].message_type = _MINIAREAMAP
_V2XOBSTACLES.fields_by_name['header'].message_type = modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2._HEADER
_V2XOBSTACLES.fields_by_name['error_code'].enum_type = modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['MiniAreaMap'] = _MINIAREAMAP
DESCRIPTOR.message_types_by_name['AbnormalInformation'] = _ABNORMALINFORMATION
DESCRIPTOR.message_types_by_name['V2XInformation'] = _V2XINFORMATION
DESCRIPTOR.message_types_by_name['V2XObstacle'] = _V2XOBSTACLE
DESCRIPTOR.message_types_by_name['V2XObstacles'] = _V2XOBSTACLES

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'modules.v2x.proto.v2x_obstacles_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.Point)
  ))
_sym_db.RegisterMessage(Point)

MiniAreaMap = _reflection.GeneratedProtocolMessageType('MiniAreaMap', (_message.Message,), dict(
  DESCRIPTOR = _MINIAREAMAP,
  __module__ = 'modules.v2x.proto.v2x_obstacles_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.MiniAreaMap)
  ))
_sym_db.RegisterMessage(MiniAreaMap)

AbnormalInformation = _reflection.GeneratedProtocolMessageType('AbnormalInformation', (_message.Message,), dict(
  DESCRIPTOR = _ABNORMALINFORMATION,
  __module__ = 'modules.v2x.proto.v2x_obstacles_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.AbnormalInformation)
  ))
_sym_db.RegisterMessage(AbnormalInformation)

V2XInformation = _reflection.GeneratedProtocolMessageType('V2XInformation', (_message.Message,), dict(
  DESCRIPTOR = _V2XINFORMATION,
  __module__ = 'modules.v2x.proto.v2x_obstacles_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.V2XInformation)
  ))
_sym_db.RegisterMessage(V2XInformation)

V2XObstacle = _reflection.GeneratedProtocolMessageType('V2XObstacle', (_message.Message,), dict(
  DESCRIPTOR = _V2XOBSTACLE,
  __module__ = 'modules.v2x.proto.v2x_obstacles_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.V2XObstacle)
  ))
_sym_db.RegisterMessage(V2XObstacle)

V2XObstacles = _reflection.GeneratedProtocolMessageType('V2XObstacles', (_message.Message,), dict(
  DESCRIPTOR = _V2XOBSTACLES,
  __module__ = 'modules.v2x.proto.v2x_obstacles_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.V2XObstacles)
  ))
_sym_db.RegisterMessage(V2XObstacles)


# @@protoc_insertion_point(module_scope)
