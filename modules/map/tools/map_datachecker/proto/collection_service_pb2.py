# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/tools/map_datachecker/proto/collection_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.map.tools.map_datachecker.proto import collection_check_message_pb2 as modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/tools/map_datachecker/proto/collection_service.proto',
  package='apollo.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n@modules/map/tools/map_datachecker/proto/collection_service.proto\x12\x0c\x61pollo.hdmap\x1a\x46modules/map/tools/map_datachecker/proto/collection_check_message.proto2\xf1\x03\n\x18\x43ollectionCheckerService\x12^\n\x13ServiceDynamicAlign\x12!.apollo.hdmap.DynamicAlignRequest\x1a\".apollo.hdmap.DynamicAlignResponse\"\x00\x12[\n\x12ServiceStaticAlign\x12 .apollo.hdmap.StaticAlignRequest\x1a!.apollo.hdmap.StaticAlignResponse\"\x00\x12X\n\x11ServiceEightRoute\x12\x1f.apollo.hdmap.EightRouteRequest\x1a .apollo.hdmap.EightRouteResponse\"\x00\x12\x61\n\x14ServiceChannelVerify\x12\".apollo.hdmap.ChannelVerifyRequest\x1a#.apollo.hdmap.ChannelVerifyResponse\"\x00\x12[\n\x12ServiceLoopsVerify\x12 .apollo.hdmap.LoopsVerifyRequest\x1a!.apollo.hdmap.LoopsVerifyResponse\"\x00')
  ,
  dependencies=[modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__check__message__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





# @@protoc_insertion_point(module_scope)
