# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rbac_payload.proto

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
  name='rbac_payload.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12rbac_payload.proto\"\x9a\x0b\n\x0bRBACPayload\x12.\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x18.RBACPayload.MessageType\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x0e\n\x06inputs\x18\x03 \x03(\t\x12\x0f\n\x07outputs\x18\x04 \x03(\t\"\xa8\n\n\x0bMessageType\x12\x1a\n\x16PROPOSE_ADD_ROLE_TASKS\x10\x00\x12\x1c\n\x18PROPOSE_ADD_ROLE_MEMBERS\x10\x01\x12\x1b\n\x17PROPOSE_ADD_ROLE_OWNERS\x10\x02\x12\x1b\n\x17PROPOSE_ADD_ROLE_ADMINS\x10\x03\x12\x1d\n\x19PROPOSE_REMOVE_ROLE_TASKS\x10\x04\x12\x1f\n\x1bPROPOSE_REMOVE_ROLE_MEMBERS\x10\x05\x12\x1e\n\x1aPROPOSE_REMOVE_ROLE_OWNERS\x10\x06\x12\x1e\n\x1aPROPOSE_REMOVE_ROLE_ADMINS\x10\x07\x12\x1a\n\x16\x43ONFIRM_ADD_ROLE_TASKS\x10\x08\x12\x1c\n\x18\x43ONFIRM_ADD_ROLE_MEMBERS\x10\t\x12\x1b\n\x17\x43ONFIRM_ADD_ROLE_OWNERS\x10\n\x12\x1b\n\x17\x43ONFIRM_ADD_ROLE_ADMINS\x10\x0b\x12\x1d\n\x19\x43ONFIRM_REMOVE_ROLE_TASKS\x10\x0c\x12\x1f\n\x1b\x43ONFIRM_REMOVE_ROLE_MEMBERS\x10\r\x12\x1e\n\x1a\x43ONFIRM_REMOVE_ROLE_OWNERS\x10\x0e\x12\x1e\n\x1a\x43ONFIRM_REMOVE_ROLE_ADMINS\x10\x0f\x12\x19\n\x15REJECT_ADD_ROLE_TASKS\x10\x10\x12\x1b\n\x17REJECT_ADD_ROLE_MEMBERS\x10\x11\x12\x1a\n\x16REJECT_ADD_ROLE_OWNERS\x10\x12\x12\x1a\n\x16REJECT_ADD_ROLE_ADMINS\x10\x13\x12\x1c\n\x18REJECT_REMOVE_ROLE_TASKS\x10\x14\x12\x1e\n\x1aREJECT_REMOVE_ROLE_MEMBERS\x10\x15\x12\x1d\n\x19REJECT_REMOVE_ROLE_OWNERS\x10\x16\x12\x1d\n\x19REJECT_REMOVE_ROLE_ADMINS\x10\x17\x12\x1b\n\x17PROPOSE_ADD_TASK_OWNERS\x10\x18\x12\x1b\n\x17PROPOSE_ADD_TASK_ADMINS\x10\x19\x12\x1e\n\x1aPROPOSE_REMOVE_TASK_OWNERS\x10\x1a\x12\x1e\n\x1aPROPOSE_REMOVE_TASK_ADMINS\x10\x1b\x12\x1b\n\x17\x43ONFIRM_ADD_TASK_OWNERS\x10\x1c\x12\x1b\n\x17\x43ONFIRM_ADD_TASK_ADMINS\x10\x1d\x12\x1e\n\x1a\x43ONFIRM_REMOVE_TASK_OWNERS\x10\x1e\x12\x1e\n\x1a\x43ONFIRM_REMOVE_TASK_ADMINS\x10\x1f\x12\x1a\n\x16REJECT_ADD_TASK_OWNERS\x10 \x12\x1a\n\x16REJECT_ADD_TASK_ADMINS\x10!\x12\x1d\n\x19REJECT_REMOVE_TASK_OWNERS\x10\"\x12\x1d\n\x19REJECT_REMOVE_TASK_ADMINS\x10#\x12\x1f\n\x1bPROPOSE_UPDATE_USER_MANAGER\x10$\x12\x1f\n\x1b\x43ONFIRM_UPDATE_USER_MANAGER\x10%\x12\x1e\n\x1aREJECT_UPDATE_USER_MANAGER\x10&\x12\x0f\n\x0b\x43REATE_ROLE\x10\'\x12\x0f\n\x0b\x43REATE_USER\x10(\x12\x0f\n\x0b\x43REATE_TASK\x10)\x12\x0f\n\x0bUPDATE_ROLE\x10*\x12\x13\n\x0fUPDATE_PROPOSAL\x10+\x12\x0f\n\x0bUPDATE_TASK\x10,\x12\x0f\n\x0bUPDATE_USER\x10-b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RBACPAYLOAD_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='RBACPayload.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_ADD_ROLE_TASKS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_ADD_ROLE_MEMBERS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_ADD_ROLE_OWNERS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_ADD_ROLE_ADMINS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_REMOVE_ROLE_TASKS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_REMOVE_ROLE_MEMBERS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_REMOVE_ROLE_OWNERS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_REMOVE_ROLE_ADMINS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ADD_ROLE_TASKS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ADD_ROLE_MEMBERS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ADD_ROLE_OWNERS', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ADD_ROLE_ADMINS', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_REMOVE_ROLE_TASKS', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_REMOVE_ROLE_MEMBERS', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_REMOVE_ROLE_OWNERS', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_REMOVE_ROLE_ADMINS', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_ADD_ROLE_TASKS', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_ADD_ROLE_MEMBERS', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_ADD_ROLE_OWNERS', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_ADD_ROLE_ADMINS', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_REMOVE_ROLE_TASKS', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_REMOVE_ROLE_MEMBERS', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_REMOVE_ROLE_OWNERS', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_REMOVE_ROLE_ADMINS', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_ADD_TASK_OWNERS', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_ADD_TASK_ADMINS', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_REMOVE_TASK_OWNERS', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_REMOVE_TASK_ADMINS', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ADD_TASK_OWNERS', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_ADD_TASK_ADMINS', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_REMOVE_TASK_OWNERS', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_REMOVE_TASK_ADMINS', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_ADD_TASK_OWNERS', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_ADD_TASK_ADMINS', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_REMOVE_TASK_OWNERS', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_REMOVE_TASK_ADMINS', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSE_UPDATE_USER_MANAGER', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRM_UPDATE_USER_MANAGER', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECT_UPDATE_USER_MANAGER', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_ROLE', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_USER', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_TASK', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_ROLE', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_PROPOSAL', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_TASK', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_USER', index=45, number=45,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=137,
  serialized_end=1457,
)
_sym_db.RegisterEnumDescriptor(_RBACPAYLOAD_MESSAGETYPE)


_RBACPAYLOAD = _descriptor.Descriptor(
  name='RBACPayload',
  full_name='RBACPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='RBACPayload.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='RBACPayload.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='RBACPayload.inputs', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='RBACPayload.outputs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RBACPAYLOAD_MESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=1457,
)

_RBACPAYLOAD.fields_by_name['message_type'].enum_type = _RBACPAYLOAD_MESSAGETYPE
_RBACPAYLOAD_MESSAGETYPE.containing_type = _RBACPAYLOAD
DESCRIPTOR.message_types_by_name['RBACPayload'] = _RBACPAYLOAD

RBACPayload = _reflection.GeneratedProtocolMessageType('RBACPayload', (_message.Message,), dict(
  DESCRIPTOR = _RBACPAYLOAD,
  __module__ = 'rbac_payload_pb2'
  # @@protoc_insertion_point(class_scope:RBACPayload)
  ))
_sym_db.RegisterMessage(RBACPayload)


# @@protoc_insertion_point(module_scope)
