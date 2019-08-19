#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/job.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/job.proto',
  package='v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cv1/job.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\"\x84\x07\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x13\n\x0bunique_name\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x0f\n\x07\x64\x65leted\x18\x07 \x01(\x08\x12\x0c\n\x04user\x18\x08 \x01(\t\x12\x12\n\ncreated_at\x18\t \x01(\t\x12\x12\n\nupdated_at\x18\n \x01(\t\x12\x12\n\nstarted_at\x18\x0b \x01(\t\x12\x13\n\x0b\x66inished_at\x18\x0c \x01(\t\x12\x0f\n\x07project\x18\r \x01(\t\x12\x12\n\nis_managed\x18\x0e \x01(\t\x12\x0c\n\x04spec\x18\x0f \x01(\t\x12\x0f\n\x07\x62\x61\x63kend\x18\x10 \x01(\t\x12\x11\n\tframework\x18\x11 \x01(\t\x12\x13\n\x0blast_status\x18\x12 \x01(\t\x12\x16\n\x0e\x63ode_reference\x18\x13 \x01(\x03\x12)\n\tresources\x18\x14 \x03(\x0b\x32\x16.v1.Job.ResourcesEntry\x12\x0e\n\x06readme\x18\x15 \x01(\t\x12\x12\n\nbookmarked\x18\x16 \x01(\x08\x12#\n\x06params\x18\x17 \x03(\x0b\x32\x13.v1.Job.ParamsEntry\x12$\n\x07run_env\x18\x18 \x03(\x0b\x32\x13.v1.Job.RunEnvEntry\x12\x11\n\tbuild_job\x18\x19 \x01(\t\x12(\n\tdata_refs\x18\x1a \x03(\x0b\x32\x15.v1.Job.DataRefsEntry\x12\x30\n\rartifact_refs\x18\x1b \x03(\x0b\x32\x19.v1.Job.ArtifactRefsEntry\x12\x10\n\x08original\x18\x1c \x01(\x03\x12\x18\n\x10\x63loning_strategy\x18\x1d \x01(\t\x1a\x30\n\x0eResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bRunEnvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rDataRefsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11\x41rtifactRefsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"n\n\tJobStatus\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\t\x12\x12\n\nupdated_at\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0f\n\x07message\x18\x06 \x01(\t\"F\n\x0eJobBodyRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x14\n\x03job\x18\x03 \x01(\x0b\x32\x07.v1.Job\"[\n\x10ListJobsResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x18\n\x07results\x18\x02 \x03(\x0b\x32\x07.v1.Job\x12\x10\n\x08previous\x18\x03 \x01(\t\x12\x0c\n\x04next\x18\x04 \x01(\t\"h\n\x17ListJobStatusesResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x1e\n\x07results\x18\x02 \x03(\x0b\x32\r.v1.JobStatus\x12\x10\n\x08previous\x18\x03 \x01(\t\x12\x0c\n\x04next\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])




_JOB_RESOURCESENTRY = _descriptor.Descriptor(
  name='ResourcesEntry',
  full_name='v1.Job.ResourcesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.Job.ResourcesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.Job.ResourcesEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=753,
  serialized_end=801,
)

_JOB_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='v1.Job.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.Job.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.Job.ParamsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=848,
)

_JOB_RUNENVENTRY = _descriptor.Descriptor(
  name='RunEnvEntry',
  full_name='v1.Job.RunEnvEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.Job.RunEnvEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.Job.RunEnvEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=895,
)

_JOB_DATAREFSENTRY = _descriptor.Descriptor(
  name='DataRefsEntry',
  full_name='v1.Job.DataRefsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.Job.DataRefsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.Job.DataRefsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=897,
  serialized_end=944,
)

_JOB_ARTIFACTREFSENTRY = _descriptor.Descriptor(
  name='ArtifactRefsEntry',
  full_name='v1.Job.ArtifactRefsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.Job.ArtifactRefsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.Job.ArtifactRefsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=946,
  serialized_end=997,
)

_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='v1.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.Job.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='v1.Job.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique_name', full_name='v1.Job.unique_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Job.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='v1.Job.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.Job.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='v1.Job.deleted', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='v1.Job.user', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='v1.Job.created_at', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='v1.Job.updated_at', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='v1.Job.started_at', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished_at', full_name='v1.Job.finished_at', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='v1.Job.project', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_managed', full_name='v1.Job.is_managed', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='v1.Job.spec', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backend', full_name='v1.Job.backend', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='framework', full_name='v1.Job.framework', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_status', full_name='v1.Job.last_status', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code_reference', full_name='v1.Job.code_reference', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='v1.Job.resources', index=19,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readme', full_name='v1.Job.readme', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmarked', full_name='v1.Job.bookmarked', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='v1.Job.params', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_env', full_name='v1.Job.run_env', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_job', full_name='v1.Job.build_job', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_refs', full_name='v1.Job.data_refs', index=25,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_refs', full_name='v1.Job.artifact_refs', index=26,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original', full_name='v1.Job.original', index=27,
      number=28, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloning_strategy', full_name='v1.Job.cloning_strategy', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_JOB_RESOURCESENTRY, _JOB_PARAMSENTRY, _JOB_RUNENVENTRY, _JOB_DATAREFSENTRY, _JOB_ARTIFACTREFSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=997,
)


_JOBSTATUS = _descriptor.Descriptor(
  name='JobStatus',
  full_name='v1.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.JobStatus.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='v1.JobStatus.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='v1.JobStatus.created_at', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='v1.JobStatus.updated_at', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v1.JobStatus.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='v1.JobStatus.message', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=999,
  serialized_end=1109,
)


_JOBBODYREQUEST = _descriptor.Descriptor(
  name='JobBodyRequest',
  full_name='v1.JobBodyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='v1.JobBodyRequest.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='v1.JobBodyRequest.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job', full_name='v1.JobBodyRequest.job', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1111,
  serialized_end=1181,
)


_LISTJOBSRESPONSE = _descriptor.Descriptor(
  name='ListJobsResponse',
  full_name='v1.ListJobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='v1.ListJobsResponse.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='v1.ListJobsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous', full_name='v1.ListJobsResponse.previous', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='v1.ListJobsResponse.next', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1183,
  serialized_end=1274,
)


_LISTJOBSTATUSESRESPONSE = _descriptor.Descriptor(
  name='ListJobStatusesResponse',
  full_name='v1.ListJobStatusesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='v1.ListJobStatusesResponse.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='v1.ListJobStatusesResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous', full_name='v1.ListJobStatusesResponse.previous', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='v1.ListJobStatusesResponse.next', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1276,
  serialized_end=1380,
)

_JOB_RESOURCESENTRY.containing_type = _JOB
_JOB_PARAMSENTRY.containing_type = _JOB
_JOB_RUNENVENTRY.containing_type = _JOB
_JOB_DATAREFSENTRY.containing_type = _JOB
_JOB_ARTIFACTREFSENTRY.containing_type = _JOB
_JOB.fields_by_name['resources'].message_type = _JOB_RESOURCESENTRY
_JOB.fields_by_name['params'].message_type = _JOB_PARAMSENTRY
_JOB.fields_by_name['run_env'].message_type = _JOB_RUNENVENTRY
_JOB.fields_by_name['data_refs'].message_type = _JOB_DATAREFSENTRY
_JOB.fields_by_name['artifact_refs'].message_type = _JOB_ARTIFACTREFSENTRY
_JOBBODYREQUEST.fields_by_name['job'].message_type = _JOB
_LISTJOBSRESPONSE.fields_by_name['results'].message_type = _JOB
_LISTJOBSTATUSESRESPONSE.fields_by_name['results'].message_type = _JOBSTATUS
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['JobStatus'] = _JOBSTATUS
DESCRIPTOR.message_types_by_name['JobBodyRequest'] = _JOBBODYREQUEST
DESCRIPTOR.message_types_by_name['ListJobsResponse'] = _LISTJOBSRESPONSE
DESCRIPTOR.message_types_by_name['ListJobStatusesResponse'] = _LISTJOBSTATUSESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {

  'ResourcesEntry' : _reflection.GeneratedProtocolMessageType('ResourcesEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOB_RESOURCESENTRY,
    '__module__' : 'v1.job_pb2'
    # @@protoc_insertion_point(class_scope:v1.Job.ResourcesEntry)
    })
  ,

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOB_PARAMSENTRY,
    '__module__' : 'v1.job_pb2'
    # @@protoc_insertion_point(class_scope:v1.Job.ParamsEntry)
    })
  ,

  'RunEnvEntry' : _reflection.GeneratedProtocolMessageType('RunEnvEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOB_RUNENVENTRY,
    '__module__' : 'v1.job_pb2'
    # @@protoc_insertion_point(class_scope:v1.Job.RunEnvEntry)
    })
  ,

  'DataRefsEntry' : _reflection.GeneratedProtocolMessageType('DataRefsEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOB_DATAREFSENTRY,
    '__module__' : 'v1.job_pb2'
    # @@protoc_insertion_point(class_scope:v1.Job.DataRefsEntry)
    })
  ,

  'ArtifactRefsEntry' : _reflection.GeneratedProtocolMessageType('ArtifactRefsEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOB_ARTIFACTREFSENTRY,
    '__module__' : 'v1.job_pb2'
    # @@protoc_insertion_point(class_scope:v1.Job.ArtifactRefsEntry)
    })
  ,
  'DESCRIPTOR' : _JOB,
  '__module__' : 'v1.job_pb2'
  # @@protoc_insertion_point(class_scope:v1.Job)
  })
_sym_db.RegisterMessage(Job)
_sym_db.RegisterMessage(Job.ResourcesEntry)
_sym_db.RegisterMessage(Job.ParamsEntry)
_sym_db.RegisterMessage(Job.RunEnvEntry)
_sym_db.RegisterMessage(Job.DataRefsEntry)
_sym_db.RegisterMessage(Job.ArtifactRefsEntry)

JobStatus = _reflection.GeneratedProtocolMessageType('JobStatus', (_message.Message,), {
  'DESCRIPTOR' : _JOBSTATUS,
  '__module__' : 'v1.job_pb2'
  # @@protoc_insertion_point(class_scope:v1.JobStatus)
  })
_sym_db.RegisterMessage(JobStatus)

JobBodyRequest = _reflection.GeneratedProtocolMessageType('JobBodyRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBBODYREQUEST,
  '__module__' : 'v1.job_pb2'
  # @@protoc_insertion_point(class_scope:v1.JobBodyRequest)
  })
_sym_db.RegisterMessage(JobBodyRequest)

ListJobsResponse = _reflection.GeneratedProtocolMessageType('ListJobsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTJOBSRESPONSE,
  '__module__' : 'v1.job_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListJobsResponse)
  })
_sym_db.RegisterMessage(ListJobsResponse)

ListJobStatusesResponse = _reflection.GeneratedProtocolMessageType('ListJobStatusesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTJOBSTATUSESRESPONSE,
  '__module__' : 'v1.job_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListJobStatusesResponse)
  })
_sym_db.RegisterMessage(ListJobStatusesResponse)


_JOB_RESOURCESENTRY._options = None
_JOB_PARAMSENTRY._options = None
_JOB_RUNENVENTRY._options = None
_JOB_DATAREFSENTRY._options = None
_JOB_ARTIFACTREFSENTRY._options = None
# @@protoc_insertion_point(module_scope)
