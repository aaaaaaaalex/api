# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TrainingService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TrainingService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15TrainingService.proto\":\n\x0cTrainRequest\x12\x11\n\tclasslist\x18\x01 \x01(\t\x12\x17\n\x0f\x63heckpoint_name\x18\x02 \x01(\t\"!\n\rTrainResponse\x12\x10\n\x08response\x18\x01 \x01(\t\":\n\x0eInstanceFilter\x12\x13\n\x0bhas_classes\x18\x01 \x01(\t\x12\x13\n\x0bnum_classes\x18\x02 \x01(\x05\"@\n\x14TrainingInstanceList\x12(\n\tinstances\x18\x01 \x03(\x0b\x32\x15.TrainingInstanceInfo\"?\n\x14TrainingInstanceInfo\x12\x14\n\x0c\x64\x61te_started\x18\x01 \x01(\t\x12\x11\n\tclasslist\x18\x02 \x01(\t2\x88\x01\n\x0fTrainingService\x12-\n\nTrainModel\x12\r.TrainRequest\x1a\x0e.TrainResponse\"\x00\x12\x46\n\x1aGetActiveTrainingInstances\x12\x0f.InstanceFilter\x1a\x15.TrainingInstanceList\"\x00\x62\x06proto3')
)




_TRAINREQUEST = _descriptor.Descriptor(
  name='TrainRequest',
  full_name='TrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classlist', full_name='TrainRequest.classlist', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_name', full_name='TrainRequest.checkpoint_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=83,
)


_TRAINRESPONSE = _descriptor.Descriptor(
  name='TrainResponse',
  full_name='TrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='TrainResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=118,
)


_INSTANCEFILTER = _descriptor.Descriptor(
  name='InstanceFilter',
  full_name='InstanceFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_classes', full_name='InstanceFilter.has_classes', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='InstanceFilter.num_classes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=178,
)


_TRAININGINSTANCELIST = _descriptor.Descriptor(
  name='TrainingInstanceList',
  full_name='TrainingInstanceList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instances', full_name='TrainingInstanceList.instances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=244,
)


_TRAININGINSTANCEINFO = _descriptor.Descriptor(
  name='TrainingInstanceInfo',
  full_name='TrainingInstanceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_started', full_name='TrainingInstanceInfo.date_started', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classlist', full_name='TrainingInstanceInfo.classlist', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=309,
)

_TRAININGINSTANCELIST.fields_by_name['instances'].message_type = _TRAININGINSTANCEINFO
DESCRIPTOR.message_types_by_name['TrainRequest'] = _TRAINREQUEST
DESCRIPTOR.message_types_by_name['TrainResponse'] = _TRAINRESPONSE
DESCRIPTOR.message_types_by_name['InstanceFilter'] = _INSTANCEFILTER
DESCRIPTOR.message_types_by_name['TrainingInstanceList'] = _TRAININGINSTANCELIST
DESCRIPTOR.message_types_by_name['TrainingInstanceInfo'] = _TRAININGINSTANCEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainRequest = _reflection.GeneratedProtocolMessageType('TrainRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRAINREQUEST,
  __module__ = 'TrainingService_pb2'
  # @@protoc_insertion_point(class_scope:TrainRequest)
  ))
_sym_db.RegisterMessage(TrainRequest)

TrainResponse = _reflection.GeneratedProtocolMessageType('TrainResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRAINRESPONSE,
  __module__ = 'TrainingService_pb2'
  # @@protoc_insertion_point(class_scope:TrainResponse)
  ))
_sym_db.RegisterMessage(TrainResponse)

InstanceFilter = _reflection.GeneratedProtocolMessageType('InstanceFilter', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCEFILTER,
  __module__ = 'TrainingService_pb2'
  # @@protoc_insertion_point(class_scope:InstanceFilter)
  ))
_sym_db.RegisterMessage(InstanceFilter)

TrainingInstanceList = _reflection.GeneratedProtocolMessageType('TrainingInstanceList', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGINSTANCELIST,
  __module__ = 'TrainingService_pb2'
  # @@protoc_insertion_point(class_scope:TrainingInstanceList)
  ))
_sym_db.RegisterMessage(TrainingInstanceList)

TrainingInstanceInfo = _reflection.GeneratedProtocolMessageType('TrainingInstanceInfo', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGINSTANCEINFO,
  __module__ = 'TrainingService_pb2'
  # @@protoc_insertion_point(class_scope:TrainingInstanceInfo)
  ))
_sym_db.RegisterMessage(TrainingInstanceInfo)



_TRAININGSERVICE = _descriptor.ServiceDescriptor(
  name='TrainingService',
  full_name='TrainingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=312,
  serialized_end=448,
  methods=[
  _descriptor.MethodDescriptor(
    name='TrainModel',
    full_name='TrainingService.TrainModel',
    index=0,
    containing_service=None,
    input_type=_TRAINREQUEST,
    output_type=_TRAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetActiveTrainingInstances',
    full_name='TrainingService.GetActiveTrainingInstances',
    index=1,
    containing_service=None,
    input_type=_INSTANCEFILTER,
    output_type=_TRAININGINSTANCELIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAININGSERVICE)

DESCRIPTOR.services_by_name['TrainingService'] = _TRAININGSERVICE

# @@protoc_insertion_point(module_scope)
