# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finterface.proto\x12\tinterface\"\x07\n\x05\x45mpty\"$\n\x0c\x45rrorMessage\x12\x14\n\x0c\x65rrorMessage\x18\x01 \x01(\t\"\x1f\n\x0b\x45nvSettings\x12\x10\n\x08settings\x18\x01 \x01(\t\"9\n\x11\x45nvInfoAndIntData\x12\x0f\n\x07\x65nvInfo\x18\x01 \x01(\t\x12\x13\n\x0bintDataList\x18\x02 \x01(\t\"~\n\x07\x43ommand\x12&\n\x02P1\x18\x01 \x01(\x0b\x32\x1a.interface.Command.actions\x12&\n\x02P2\x18\x02 \x01(\x0b\x32\x1a.interface.Command.actions\x1a#\n\x07\x61\x63tions\x12\x0b\n\x03mov\x18\x01 \x01(\x05\x12\x0b\n\x03\x61tt\x18\x02 \x01(\x05\"\xb0\x01\n\x03Obs\x12\x0e\n\x06intVar\x18\x01 \x01(\t\x12\x30\n\x0e\x64oneConditions\x18\x02 \x01(\x0b\x32\x18.interface.Obs.boolFlags\x12\x0e\n\x06player\x18\x03 \x01(\t\x12\r\n\x05\x66rame\x18\x04 \x01(\x0c\x1aH\n\tboolFlags\x12\r\n\x05round\x18\x01 \x01(\x08\x12\r\n\x05stage\x18\x02 \x01(\x08\x12\x0c\n\x04game\x18\x03 \x01(\x08\x12\x0f\n\x07\x65pisode\x18\x04 \x01(\x08\x32\xc3\x02\n\tEnvServer\x12\x37\n\x08GetError\x12\x10.interface.Empty\x1a\x17.interface.ErrorMessage\"\x00\x12\x41\n\x07\x45nvInit\x12\x16.interface.EnvSettings\x1a\x1c.interface.EnvInfoAndIntData\"\x00\x12+\n\x05Reset\x12\x10.interface.Empty\x1a\x0e.interface.Obs\"\x00\x12.\n\x06Step1P\x12\x12.interface.Command\x1a\x0e.interface.Obs\"\x00\x12.\n\x06Step2P\x12\x12.interface.Command\x1a\x0e.interface.Obs\"\x00\x12-\n\x05\x43lose\x12\x10.interface.Empty\x1a\x10.interface.Empty\"\x00\x42\x06\xa2\x02\x03HLWb\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_ERRORMESSAGE = DESCRIPTOR.message_types_by_name['ErrorMessage']
_ENVSETTINGS = DESCRIPTOR.message_types_by_name['EnvSettings']
_ENVINFOANDINTDATA = DESCRIPTOR.message_types_by_name['EnvInfoAndIntData']
_COMMAND = DESCRIPTOR.message_types_by_name['Command']
_COMMAND_ACTIONS = _COMMAND.nested_types_by_name['actions']
_OBS = DESCRIPTOR.message_types_by_name['Obs']
_OBS_BOOLFLAGS = _OBS.nested_types_by_name['boolFlags']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Empty)
  })
_sym_db.RegisterMessage(Empty)

ErrorMessage = _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), {
  'DESCRIPTOR' : _ERRORMESSAGE,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.ErrorMessage)
  })
_sym_db.RegisterMessage(ErrorMessage)

EnvSettings = _reflection.GeneratedProtocolMessageType('EnvSettings', (_message.Message,), {
  'DESCRIPTOR' : _ENVSETTINGS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.EnvSettings)
  })
_sym_db.RegisterMessage(EnvSettings)

EnvInfoAndIntData = _reflection.GeneratedProtocolMessageType('EnvInfoAndIntData', (_message.Message,), {
  'DESCRIPTOR' : _ENVINFOANDINTDATA,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.EnvInfoAndIntData)
  })
_sym_db.RegisterMessage(EnvInfoAndIntData)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {

  'actions' : _reflection.GeneratedProtocolMessageType('actions', (_message.Message,), {
    'DESCRIPTOR' : _COMMAND_ACTIONS,
    '__module__' : 'interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.Command.actions)
    })
  ,
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Command)
  })
_sym_db.RegisterMessage(Command)
_sym_db.RegisterMessage(Command.actions)

Obs = _reflection.GeneratedProtocolMessageType('Obs', (_message.Message,), {

  'boolFlags' : _reflection.GeneratedProtocolMessageType('boolFlags', (_message.Message,), {
    'DESCRIPTOR' : _OBS_BOOLFLAGS,
    '__module__' : 'interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.Obs.boolFlags)
    })
  ,
  'DESCRIPTOR' : _OBS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Obs)
  })
_sym_db.RegisterMessage(Obs)
_sym_db.RegisterMessage(Obs.boolFlags)

_ENVSERVER = DESCRIPTOR.services_by_name['EnvServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\242\002\003HLW'
  _EMPTY._serialized_start=30
  _EMPTY._serialized_end=37
  _ERRORMESSAGE._serialized_start=39
  _ERRORMESSAGE._serialized_end=75
  _ENVSETTINGS._serialized_start=77
  _ENVSETTINGS._serialized_end=108
  _ENVINFOANDINTDATA._serialized_start=110
  _ENVINFOANDINTDATA._serialized_end=167
  _COMMAND._serialized_start=169
  _COMMAND._serialized_end=295
  _COMMAND_ACTIONS._serialized_start=260
  _COMMAND_ACTIONS._serialized_end=295
  _OBS._serialized_start=298
  _OBS._serialized_end=474
  _OBS_BOOLFLAGS._serialized_start=402
  _OBS_BOOLFLAGS._serialized_end=474
  _ENVSERVER._serialized_start=477
  _ENVSERVER._serialized_end=800
# @@protoc_insertion_point(module_scope)
