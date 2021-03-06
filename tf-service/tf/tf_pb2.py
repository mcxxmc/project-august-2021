# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tf.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08tf.proto\"\x0c\n\nTFStandard\"#\n\x05Image\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"$\n\nImageArray\x12\x16\n\x06Images\x18\x01 \x03(\x0b\x32\x06.Image\"(\n\nPrediction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04pred\x18\x02 \x01(\x08\"3\n\x0fPredictionArray\x12 \n\x0bPredictions\x18\x01 \x03(\x0b\x32\x0b.Prediction2o\n\x0c\x43ommunicator\x12+\n\rRequestImages\x12\x0b.TFStandard\x1a\x0b.ImageArray\"\x00\x12\x32\n\x0fPostPredictions\x12\x10.PredictionArray\x1a\x0b.TFStandard\"\x00\x62\x06proto3'
)




_TFSTANDARD = _descriptor.Descriptor(
  name='TFStandard',
  full_name='TFStandard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=12,
  serialized_end=24,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Image.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='Image.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=61,
)


_IMAGEARRAY = _descriptor.Descriptor(
  name='ImageArray',
  full_name='ImageArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Images', full_name='ImageArray.Images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=99,
)


_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Prediction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pred', full_name='Prediction.pred', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=101,
  serialized_end=141,
)


_PREDICTIONARRAY = _descriptor.Descriptor(
  name='PredictionArray',
  full_name='PredictionArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Predictions', full_name='PredictionArray.Predictions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=143,
  serialized_end=194,
)

_IMAGEARRAY.fields_by_name['Images'].message_type = _IMAGE
_PREDICTIONARRAY.fields_by_name['Predictions'].message_type = _PREDICTION
DESCRIPTOR.message_types_by_name['TFStandard'] = _TFSTANDARD
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['ImageArray'] = _IMAGEARRAY
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
DESCRIPTOR.message_types_by_name['PredictionArray'] = _PREDICTIONARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TFStandard = _reflection.GeneratedProtocolMessageType('TFStandard', (_message.Message,), {
  'DESCRIPTOR' : _TFSTANDARD,
  '__module__' : 'tf_pb2'
  # @@protoc_insertion_point(class_scope:TFStandard)
  })
_sym_db.RegisterMessage(TFStandard)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'tf_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)

ImageArray = _reflection.GeneratedProtocolMessageType('ImageArray', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEARRAY,
  '__module__' : 'tf_pb2'
  # @@protoc_insertion_point(class_scope:ImageArray)
  })
_sym_db.RegisterMessage(ImageArray)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'tf_pb2'
  # @@protoc_insertion_point(class_scope:Prediction)
  })
_sym_db.RegisterMessage(Prediction)

PredictionArray = _reflection.GeneratedProtocolMessageType('PredictionArray', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONARRAY,
  '__module__' : 'tf_pb2'
  # @@protoc_insertion_point(class_scope:PredictionArray)
  })
_sym_db.RegisterMessage(PredictionArray)



_COMMUNICATOR = _descriptor.ServiceDescriptor(
  name='Communicator',
  full_name='Communicator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=196,
  serialized_end=307,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestImages',
    full_name='Communicator.RequestImages',
    index=0,
    containing_service=None,
    input_type=_TFSTANDARD,
    output_type=_IMAGEARRAY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostPredictions',
    full_name='Communicator.PostPredictions',
    index=1,
    containing_service=None,
    input_type=_PREDICTIONARRAY,
    output_type=_TFSTANDARD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMUNICATOR)

DESCRIPTOR.services_by_name['Communicator'] = _COMMUNICATOR

# @@protoc_insertion_point(module_scope)
