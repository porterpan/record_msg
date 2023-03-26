# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/dreamview/proto/hmi_mode.proto

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
  name='modules/dreamview/proto/hmi_mode.proto',
  package='apollo.dreamview',
  syntax='proto2',
  serialized_pb=_b('\n&modules/dreamview/proto/hmi_mode.proto\x12\x10\x61pollo.dreamview\"0\n\x14ProcessMonitorConfig\x12\x18\n\x10\x63ommand_keywords\x18\x01 \x03(\t\"(\n\x13ModuleMonitorConfig\x12\x11\n\tnode_name\x18\x01 \x03(\t\"\x9d\x01\n\x14\x43hannelMonitorConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0b\x64\x65lay_fatal\x18\x02 \x01(\x01:\x01\x33\x12\x18\n\x10mandatory_fields\x18\x03 \x03(\t\x12 \n\x15min_frequency_allowed\x18\x04 \x01(\x01:\x01\x30\x12#\n\x15max_frequency_allowed\x18\x05 \x01(\x01:\x04\x31\x30\x30\x30\"\xce\x05\n\x15ResourceMonitorConfig\x12\x46\n\x0b\x64isk_spaces\x18\x01 \x03(\x0b\x32\x31.apollo.dreamview.ResourceMonitorConfig.DiskSpace\x12\x44\n\ncpu_usages\x18\x02 \x03(\x0b\x32\x30.apollo.dreamview.ResourceMonitorConfig.CPUUsage\x12J\n\rmemory_usages\x18\x03 \x03(\x0b\x32\x33.apollo.dreamview.ResourceMonitorConfig.MemoryUsage\x12J\n\x10\x64isk_load_usages\x18\x04 \x03(\x0b\x32\x30.apollo.dreamview.ResourceMonitorConfig.DiskLoad\x1a_\n\tDiskSpace\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\"\n\x1ainsufficient_space_warning\x18\x02 \x01(\x05\x12 \n\x18insufficient_space_error\x18\x03 \x01(\x05\x1a\x62\n\x08\x43PUUsage\x12\x1e\n\x16high_cpu_usage_warning\x18\x01 \x01(\x02\x12\x1c\n\x14high_cpu_usage_error\x18\x02 \x01(\x02\x12\x18\n\x10process_dag_path\x18\x03 \x01(\t\x1ak\n\x0bMemoryUsage\x12!\n\x19high_memory_usage_warning\x18\x01 \x01(\x05\x12\x1f\n\x17high_memory_usage_error\x18\x02 \x01(\x05\x12\x18\n\x10process_dag_path\x18\x03 \x01(\t\x1a]\n\x08\x44iskLoad\x12\x1e\n\x16high_disk_load_warning\x18\x01 \x01(\x05\x12\x1c\n\x14high_disk_load_error\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\t\"\x9b\x02\n\x12MonitoredComponent\x12\x37\n\x07process\x18\x01 \x01(\x0b\x32&.apollo.dreamview.ProcessMonitorConfig\x12\x37\n\x07\x63hannel\x18\x02 \x01(\x0b\x32&.apollo.dreamview.ChannelMonitorConfig\x12\x39\n\x08resource\x18\x03 \x01(\x0b\x32\'.apollo.dreamview.ResourceMonitorConfig\x12!\n\x13required_for_safety\x18\x04 \x01(\x08:\x04true\x12\x35\n\x06module\x18\x05 \x01(\x0b\x32%.apollo.dreamview.ModuleMonitorConfig\"\xa0\x01\n\x06Module\x12\x15\n\rstart_command\x18\x01 \x01(\t\x12\x14\n\x0cstop_command\x18\x02 \x01(\t\x12\x46\n\x16process_monitor_config\x18\x03 \x01(\x0b\x32&.apollo.dreamview.ProcessMonitorConfig\x12!\n\x13required_for_safety\x18\x04 \x01(\x08:\x04true\"Z\n\x0b\x43yberModule\x12\x11\n\tdag_files\x18\x01 \x03(\t\x12!\n\x13required_for_safety\x18\x02 \x01(\x08:\x04true\x12\x15\n\rprocess_group\x18\x03 \x01(\t\"\x82\x05\n\x07HMIMode\x12\x42\n\rcyber_modules\x18\x01 \x03(\x0b\x32+.apollo.dreamview.HMIMode.CyberModulesEntry\x12\x37\n\x07modules\x18\x02 \x03(\x0b\x32&.apollo.dreamview.HMIMode.ModulesEntry\x12P\n\x14monitored_components\x18\x03 \x03(\x0b\x32\x32.apollo.dreamview.HMIMode.MonitoredComponentsEntry\x12H\n\x10other_components\x18\x04 \x03(\x0b\x32..apollo.dreamview.HMIMode.OtherComponentsEntry\x1aR\n\x11\x43yberModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.apollo.dreamview.CyberModule:\x02\x38\x01\x1aH\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.apollo.dreamview.Module:\x02\x38\x01\x1a`\n\x18MonitoredComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.apollo.dreamview.MonitoredComponent:\x02\x38\x01\x1a^\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.apollo.dreamview.ProcessMonitorConfig:\x02\x38\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROCESSMONITORCONFIG = _descriptor.Descriptor(
  name='ProcessMonitorConfig',
  full_name='apollo.dreamview.ProcessMonitorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_keywords', full_name='apollo.dreamview.ProcessMonitorConfig.command_keywords', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=60,
  serialized_end=108,
)


_MODULEMONITORCONFIG = _descriptor.Descriptor(
  name='ModuleMonitorConfig',
  full_name='apollo.dreamview.ModuleMonitorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='apollo.dreamview.ModuleMonitorConfig.node_name', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=110,
  serialized_end=150,
)


_CHANNELMONITORCONFIG = _descriptor.Descriptor(
  name='ChannelMonitorConfig',
  full_name='apollo.dreamview.ChannelMonitorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.dreamview.ChannelMonitorConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay_fatal', full_name='apollo.dreamview.ChannelMonitorConfig.delay_fatal', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mandatory_fields', full_name='apollo.dreamview.ChannelMonitorConfig.mandatory_fields', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_frequency_allowed', full_name='apollo.dreamview.ChannelMonitorConfig.min_frequency_allowed', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_frequency_allowed', full_name='apollo.dreamview.ChannelMonitorConfig.max_frequency_allowed', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1000),
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
  serialized_start=153,
  serialized_end=310,
)


_RESOURCEMONITORCONFIG_DISKSPACE = _descriptor.Descriptor(
  name='DiskSpace',
  full_name='apollo.dreamview.ResourceMonitorConfig.DiskSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='apollo.dreamview.ResourceMonitorConfig.DiskSpace.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insufficient_space_warning', full_name='apollo.dreamview.ResourceMonitorConfig.DiskSpace.insufficient_space_warning', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insufficient_space_error', full_name='apollo.dreamview.ResourceMonitorConfig.DiskSpace.insufficient_space_error', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=632,
  serialized_end=727,
)

_RESOURCEMONITORCONFIG_CPUUSAGE = _descriptor.Descriptor(
  name='CPUUsage',
  full_name='apollo.dreamview.ResourceMonitorConfig.CPUUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='high_cpu_usage_warning', full_name='apollo.dreamview.ResourceMonitorConfig.CPUUsage.high_cpu_usage_warning', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_cpu_usage_error', full_name='apollo.dreamview.ResourceMonitorConfig.CPUUsage.high_cpu_usage_error', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_dag_path', full_name='apollo.dreamview.ResourceMonitorConfig.CPUUsage.process_dag_path', index=2,
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
  serialized_start=729,
  serialized_end=827,
)

_RESOURCEMONITORCONFIG_MEMORYUSAGE = _descriptor.Descriptor(
  name='MemoryUsage',
  full_name='apollo.dreamview.ResourceMonitorConfig.MemoryUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='high_memory_usage_warning', full_name='apollo.dreamview.ResourceMonitorConfig.MemoryUsage.high_memory_usage_warning', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_memory_usage_error', full_name='apollo.dreamview.ResourceMonitorConfig.MemoryUsage.high_memory_usage_error', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_dag_path', full_name='apollo.dreamview.ResourceMonitorConfig.MemoryUsage.process_dag_path', index=2,
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
  serialized_start=829,
  serialized_end=936,
)

_RESOURCEMONITORCONFIG_DISKLOAD = _descriptor.Descriptor(
  name='DiskLoad',
  full_name='apollo.dreamview.ResourceMonitorConfig.DiskLoad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='high_disk_load_warning', full_name='apollo.dreamview.ResourceMonitorConfig.DiskLoad.high_disk_load_warning', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_disk_load_error', full_name='apollo.dreamview.ResourceMonitorConfig.DiskLoad.high_disk_load_error', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='apollo.dreamview.ResourceMonitorConfig.DiskLoad.device_name', index=2,
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
  serialized_start=938,
  serialized_end=1031,
)

_RESOURCEMONITORCONFIG = _descriptor.Descriptor(
  name='ResourceMonitorConfig',
  full_name='apollo.dreamview.ResourceMonitorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_spaces', full_name='apollo.dreamview.ResourceMonitorConfig.disk_spaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_usages', full_name='apollo.dreamview.ResourceMonitorConfig.cpu_usages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_usages', full_name='apollo.dreamview.ResourceMonitorConfig.memory_usages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_load_usages', full_name='apollo.dreamview.ResourceMonitorConfig.disk_load_usages', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESOURCEMONITORCONFIG_DISKSPACE, _RESOURCEMONITORCONFIG_CPUUSAGE, _RESOURCEMONITORCONFIG_MEMORYUSAGE, _RESOURCEMONITORCONFIG_DISKLOAD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=1031,
)


_MONITOREDCOMPONENT = _descriptor.Descriptor(
  name='MonitoredComponent',
  full_name='apollo.dreamview.MonitoredComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='process', full_name='apollo.dreamview.MonitoredComponent.process', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='apollo.dreamview.MonitoredComponent.channel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='apollo.dreamview.MonitoredComponent.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_for_safety', full_name='apollo.dreamview.MonitoredComponent.required_for_safety', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='module', full_name='apollo.dreamview.MonitoredComponent.module', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=1034,
  serialized_end=1317,
)


_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='apollo.dreamview.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_command', full_name='apollo.dreamview.Module.start_command', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_command', full_name='apollo.dreamview.Module.stop_command', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_monitor_config', full_name='apollo.dreamview.Module.process_monitor_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_for_safety', full_name='apollo.dreamview.Module.required_for_safety', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=1320,
  serialized_end=1480,
)


_CYBERMODULE = _descriptor.Descriptor(
  name='CyberModule',
  full_name='apollo.dreamview.CyberModule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dag_files', full_name='apollo.dreamview.CyberModule.dag_files', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_for_safety', full_name='apollo.dreamview.CyberModule.required_for_safety', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_group', full_name='apollo.dreamview.CyberModule.process_group', index=2,
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
  serialized_start=1482,
  serialized_end=1572,
)


_HMIMODE_CYBERMODULESENTRY = _descriptor.Descriptor(
  name='CyberModulesEntry',
  full_name='apollo.dreamview.HMIMode.CyberModulesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIMode.CyberModulesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIMode.CyberModulesEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1867,
  serialized_end=1949,
)

_HMIMODE_MODULESENTRY = _descriptor.Descriptor(
  name='ModulesEntry',
  full_name='apollo.dreamview.HMIMode.ModulesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIMode.ModulesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIMode.ModulesEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1951,
  serialized_end=2023,
)

_HMIMODE_MONITOREDCOMPONENTSENTRY = _descriptor.Descriptor(
  name='MonitoredComponentsEntry',
  full_name='apollo.dreamview.HMIMode.MonitoredComponentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIMode.MonitoredComponentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIMode.MonitoredComponentsEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2025,
  serialized_end=2121,
)

_HMIMODE_OTHERCOMPONENTSENTRY = _descriptor.Descriptor(
  name='OtherComponentsEntry',
  full_name='apollo.dreamview.HMIMode.OtherComponentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apollo.dreamview.HMIMode.OtherComponentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='apollo.dreamview.HMIMode.OtherComponentsEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2123,
  serialized_end=2217,
)

_HMIMODE = _descriptor.Descriptor(
  name='HMIMode',
  full_name='apollo.dreamview.HMIMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cyber_modules', full_name='apollo.dreamview.HMIMode.cyber_modules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modules', full_name='apollo.dreamview.HMIMode.modules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monitored_components', full_name='apollo.dreamview.HMIMode.monitored_components', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_components', full_name='apollo.dreamview.HMIMode.other_components', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HMIMODE_CYBERMODULESENTRY, _HMIMODE_MODULESENTRY, _HMIMODE_MONITOREDCOMPONENTSENTRY, _HMIMODE_OTHERCOMPONENTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1575,
  serialized_end=2217,
)

_RESOURCEMONITORCONFIG_DISKSPACE.containing_type = _RESOURCEMONITORCONFIG
_RESOURCEMONITORCONFIG_CPUUSAGE.containing_type = _RESOURCEMONITORCONFIG
_RESOURCEMONITORCONFIG_MEMORYUSAGE.containing_type = _RESOURCEMONITORCONFIG
_RESOURCEMONITORCONFIG_DISKLOAD.containing_type = _RESOURCEMONITORCONFIG
_RESOURCEMONITORCONFIG.fields_by_name['disk_spaces'].message_type = _RESOURCEMONITORCONFIG_DISKSPACE
_RESOURCEMONITORCONFIG.fields_by_name['cpu_usages'].message_type = _RESOURCEMONITORCONFIG_CPUUSAGE
_RESOURCEMONITORCONFIG.fields_by_name['memory_usages'].message_type = _RESOURCEMONITORCONFIG_MEMORYUSAGE
_RESOURCEMONITORCONFIG.fields_by_name['disk_load_usages'].message_type = _RESOURCEMONITORCONFIG_DISKLOAD
_MONITOREDCOMPONENT.fields_by_name['process'].message_type = _PROCESSMONITORCONFIG
_MONITOREDCOMPONENT.fields_by_name['channel'].message_type = _CHANNELMONITORCONFIG
_MONITOREDCOMPONENT.fields_by_name['resource'].message_type = _RESOURCEMONITORCONFIG
_MONITOREDCOMPONENT.fields_by_name['module'].message_type = _MODULEMONITORCONFIG
_MODULE.fields_by_name['process_monitor_config'].message_type = _PROCESSMONITORCONFIG
_HMIMODE_CYBERMODULESENTRY.fields_by_name['value'].message_type = _CYBERMODULE
_HMIMODE_CYBERMODULESENTRY.containing_type = _HMIMODE
_HMIMODE_MODULESENTRY.fields_by_name['value'].message_type = _MODULE
_HMIMODE_MODULESENTRY.containing_type = _HMIMODE
_HMIMODE_MONITOREDCOMPONENTSENTRY.fields_by_name['value'].message_type = _MONITOREDCOMPONENT
_HMIMODE_MONITOREDCOMPONENTSENTRY.containing_type = _HMIMODE
_HMIMODE_OTHERCOMPONENTSENTRY.fields_by_name['value'].message_type = _PROCESSMONITORCONFIG
_HMIMODE_OTHERCOMPONENTSENTRY.containing_type = _HMIMODE
_HMIMODE.fields_by_name['cyber_modules'].message_type = _HMIMODE_CYBERMODULESENTRY
_HMIMODE.fields_by_name['modules'].message_type = _HMIMODE_MODULESENTRY
_HMIMODE.fields_by_name['monitored_components'].message_type = _HMIMODE_MONITOREDCOMPONENTSENTRY
_HMIMODE.fields_by_name['other_components'].message_type = _HMIMODE_OTHERCOMPONENTSENTRY
DESCRIPTOR.message_types_by_name['ProcessMonitorConfig'] = _PROCESSMONITORCONFIG
DESCRIPTOR.message_types_by_name['ModuleMonitorConfig'] = _MODULEMONITORCONFIG
DESCRIPTOR.message_types_by_name['ChannelMonitorConfig'] = _CHANNELMONITORCONFIG
DESCRIPTOR.message_types_by_name['ResourceMonitorConfig'] = _RESOURCEMONITORCONFIG
DESCRIPTOR.message_types_by_name['MonitoredComponent'] = _MONITOREDCOMPONENT
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['CyberModule'] = _CYBERMODULE
DESCRIPTOR.message_types_by_name['HMIMode'] = _HMIMODE

ProcessMonitorConfig = _reflection.GeneratedProtocolMessageType('ProcessMonitorConfig', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSMONITORCONFIG,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.ProcessMonitorConfig)
  ))
_sym_db.RegisterMessage(ProcessMonitorConfig)

ModuleMonitorConfig = _reflection.GeneratedProtocolMessageType('ModuleMonitorConfig', (_message.Message,), dict(
  DESCRIPTOR = _MODULEMONITORCONFIG,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.ModuleMonitorConfig)
  ))
_sym_db.RegisterMessage(ModuleMonitorConfig)

ChannelMonitorConfig = _reflection.GeneratedProtocolMessageType('ChannelMonitorConfig', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELMONITORCONFIG,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.ChannelMonitorConfig)
  ))
_sym_db.RegisterMessage(ChannelMonitorConfig)

ResourceMonitorConfig = _reflection.GeneratedProtocolMessageType('ResourceMonitorConfig', (_message.Message,), dict(

  DiskSpace = _reflection.GeneratedProtocolMessageType('DiskSpace', (_message.Message,), dict(
    DESCRIPTOR = _RESOURCEMONITORCONFIG_DISKSPACE,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.ResourceMonitorConfig.DiskSpace)
    ))
  ,

  CPUUsage = _reflection.GeneratedProtocolMessageType('CPUUsage', (_message.Message,), dict(
    DESCRIPTOR = _RESOURCEMONITORCONFIG_CPUUSAGE,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.ResourceMonitorConfig.CPUUsage)
    ))
  ,

  MemoryUsage = _reflection.GeneratedProtocolMessageType('MemoryUsage', (_message.Message,), dict(
    DESCRIPTOR = _RESOURCEMONITORCONFIG_MEMORYUSAGE,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.ResourceMonitorConfig.MemoryUsage)
    ))
  ,

  DiskLoad = _reflection.GeneratedProtocolMessageType('DiskLoad', (_message.Message,), dict(
    DESCRIPTOR = _RESOURCEMONITORCONFIG_DISKLOAD,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.ResourceMonitorConfig.DiskLoad)
    ))
  ,
  DESCRIPTOR = _RESOURCEMONITORCONFIG,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.ResourceMonitorConfig)
  ))
_sym_db.RegisterMessage(ResourceMonitorConfig)
_sym_db.RegisterMessage(ResourceMonitorConfig.DiskSpace)
_sym_db.RegisterMessage(ResourceMonitorConfig.CPUUsage)
_sym_db.RegisterMessage(ResourceMonitorConfig.MemoryUsage)
_sym_db.RegisterMessage(ResourceMonitorConfig.DiskLoad)

MonitoredComponent = _reflection.GeneratedProtocolMessageType('MonitoredComponent', (_message.Message,), dict(
  DESCRIPTOR = _MONITOREDCOMPONENT,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.MonitoredComponent)
  ))
_sym_db.RegisterMessage(MonitoredComponent)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), dict(
  DESCRIPTOR = _MODULE,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.Module)
  ))
_sym_db.RegisterMessage(Module)

CyberModule = _reflection.GeneratedProtocolMessageType('CyberModule', (_message.Message,), dict(
  DESCRIPTOR = _CYBERMODULE,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.CyberModule)
  ))
_sym_db.RegisterMessage(CyberModule)

HMIMode = _reflection.GeneratedProtocolMessageType('HMIMode', (_message.Message,), dict(

  CyberModulesEntry = _reflection.GeneratedProtocolMessageType('CyberModulesEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMIMODE_CYBERMODULESENTRY,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIMode.CyberModulesEntry)
    ))
  ,

  ModulesEntry = _reflection.GeneratedProtocolMessageType('ModulesEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMIMODE_MODULESENTRY,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIMode.ModulesEntry)
    ))
  ,

  MonitoredComponentsEntry = _reflection.GeneratedProtocolMessageType('MonitoredComponentsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMIMODE_MONITOREDCOMPONENTSENTRY,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIMode.MonitoredComponentsEntry)
    ))
  ,

  OtherComponentsEntry = _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HMIMODE_OTHERCOMPONENTSENTRY,
    __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIMode.OtherComponentsEntry)
    ))
  ,
  DESCRIPTOR = _HMIMODE,
  __module__ = 'modules.dreamview.proto.hmi_mode_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIMode)
  ))
_sym_db.RegisterMessage(HMIMode)
_sym_db.RegisterMessage(HMIMode.CyberModulesEntry)
_sym_db.RegisterMessage(HMIMode.ModulesEntry)
_sym_db.RegisterMessage(HMIMode.MonitoredComponentsEntry)
_sym_db.RegisterMessage(HMIMode.OtherComponentsEntry)


_HMIMODE_CYBERMODULESENTRY.has_options = True
_HMIMODE_CYBERMODULESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_HMIMODE_MODULESENTRY.has_options = True
_HMIMODE_MODULESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_HMIMODE_MONITOREDCOMPONENTSENTRY.has_options = True
_HMIMODE_MONITOREDCOMPONENTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_HMIMODE_OTHERCOMPONENTSENTRY.has_options = True
_HMIMODE_OTHERCOMPONENTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
