# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cyber/proto/role_attributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cyber.proto import qos_profile_pb2 as cyber_dot_proto_dot_qos__profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cyber/proto/role_attributes.proto',
  package='apollo.cyber.proto',
  syntax='proto2',
  serialized_pb=_b('\n!cyber/proto/role_attributes.proto\x12\x12\x61pollo.cyber.proto\x1a\x1d\x63yber/proto/qos_profile.proto\"&\n\nSocketAddr\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"\xe0\x02\n\x0eRoleAttributes\x12\x11\n\thost_name\x18\x01 \x01(\t\x12\x0f\n\x07host_ip\x18\x02 \x01(\t\x12\x12\n\nprocess_id\x18\x03 \x01(\x05\x12\x11\n\tnode_name\x18\x04 \x01(\t\x12\x0f\n\x07node_id\x18\x05 \x01(\x04\x12\x14\n\x0c\x63hannel_name\x18\x06 \x01(\t\x12\x12\n\nchannel_id\x18\x07 \x01(\x04\x12\x14\n\x0cmessage_type\x18\x08 \x01(\t\x12\x12\n\nproto_desc\x18\t \x01(\x0c\x12\n\n\x02id\x18\n \x01(\x04\x12\x33\n\x0bqos_profile\x18\x0b \x01(\x0b\x32\x1e.apollo.cyber.proto.QosProfile\x12\x33\n\x0bsocket_addr\x18\x0c \x01(\x0b\x32\x1e.apollo.cyber.proto.SocketAddr\x12\x14\n\x0cservice_name\x18\r \x01(\t\x12\x12\n\nservice_id\x18\x0e \x01(\x04')
  ,
  dependencies=[cyber_dot_proto_dot_qos__profile__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SOCKETADDR = _descriptor.Descriptor(
  name='SocketAddr',
  full_name='apollo.cyber.proto.SocketAddr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='apollo.cyber.proto.SocketAddr.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='apollo.cyber.proto.SocketAddr.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=88,
  serialized_end=126,
)


_ROLEATTRIBUTES = _descriptor.Descriptor(
  name='RoleAttributes',
  full_name='apollo.cyber.proto.RoleAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_name', full_name='apollo.cyber.proto.RoleAttributes.host_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host_ip', full_name='apollo.cyber.proto.RoleAttributes.host_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_id', full_name='apollo.cyber.proto.RoleAttributes.process_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='apollo.cyber.proto.RoleAttributes.node_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='apollo.cyber.proto.RoleAttributes.node_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_name', full_name='apollo.cyber.proto.RoleAttributes.channel_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='apollo.cyber.proto.RoleAttributes.channel_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='apollo.cyber.proto.RoleAttributes.message_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto_desc', full_name='apollo.cyber.proto.RoleAttributes.proto_desc', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.cyber.proto.RoleAttributes.id', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qos_profile', full_name='apollo.cyber.proto.RoleAttributes.qos_profile', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='socket_addr', full_name='apollo.cyber.proto.RoleAttributes.socket_addr', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='apollo.cyber.proto.RoleAttributes.service_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_id', full_name='apollo.cyber.proto.RoleAttributes.service_id', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=129,
  serialized_end=481,
)

_ROLEATTRIBUTES.fields_by_name['qos_profile'].message_type = cyber_dot_proto_dot_qos__profile__pb2._QOSPROFILE
_ROLEATTRIBUTES.fields_by_name['socket_addr'].message_type = _SOCKETADDR
DESCRIPTOR.message_types_by_name['SocketAddr'] = _SOCKETADDR
DESCRIPTOR.message_types_by_name['RoleAttributes'] = _ROLEATTRIBUTES

SocketAddr = _reflection.GeneratedProtocolMessageType('SocketAddr', (_message.Message,), dict(
  DESCRIPTOR = _SOCKETADDR,
  __module__ = 'cyber.proto.role_attributes_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.SocketAddr)
  ))
_sym_db.RegisterMessage(SocketAddr)

RoleAttributes = _reflection.GeneratedProtocolMessageType('RoleAttributes', (_message.Message,), dict(
  DESCRIPTOR = _ROLEATTRIBUTES,
  __module__ = 'cyber.proto.role_attributes_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.RoleAttributes)
  ))
_sym_db.RegisterMessage(RoleAttributes)


# @@protoc_insertion_point(module_scope)
