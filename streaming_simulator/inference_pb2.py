# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: inference.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'inference.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finference.proto\"\x1d\n\x0cImageRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\"#\n\x12PredictionResponse\x12\r\n\x05label\x18\x01 \x01(\t2A\n\x10InferenceService\x12-\n\x07Predict\x12\r.ImageRequest\x1a\x13.PredictionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEREQUEST']._serialized_start=19
  _globals['_IMAGEREQUEST']._serialized_end=48
  _globals['_PREDICTIONRESPONSE']._serialized_start=50
  _globals['_PREDICTIONRESPONSE']._serialized_end=85
  _globals['_INFERENCESERVICE']._serialized_start=87
  _globals['_INFERENCESERVICE']._serialized_end=152
# @@protoc_insertion_point(module_scope)
