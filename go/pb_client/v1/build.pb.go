// Copyright 2019 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by protoc-gen-go. DO NOT EDIT.
// source: v1/build.proto

package v1

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/golang/protobuf/ptypes/any"
	_ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// Build specification
type Build struct {
	// Unique integer identifier
	Id int64 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	// UUID
	Uuid string `protobuf:"bytes,2,opt,name=uuid,proto3" json:"uuid,omitempty"`
	// Unique name generated
	UniqueName string `protobuf:"bytes,3,opt,name=unique_name,json=uniqueName,proto3" json:"unique_name,omitempty"`
	// Optional name
	Name string `protobuf:"bytes,4,opt,name=name,proto3" json:"name,omitempty"`
	// Optional description
	Description string `protobuf:"bytes,5,opt,name=description,proto3" json:"description,omitempty"`
	// Optional Tags of this entity
	Tags []string `protobuf:"bytes,6,rep,name=tags,proto3" json:"tags,omitempty"`
	// Optional if the entity has been deleted
	Deleted bool `protobuf:"varint,7,opt,name=deleted,proto3" json:"deleted,omitempty"`
	// Required name of user started this entity
	User string `protobuf:"bytes,8,opt,name=user,proto3" json:"user,omitempty"`
	// Optional time when the entityt was created
	CreatedAt string `protobuf:"bytes,9,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	// Optional last time the entity was updated
	UpdatedAt string `protobuf:"bytes,10,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	// Optional last time the entity was started
	StartedAt string `protobuf:"bytes,11,opt,name=started_at,json=startedAt,proto3" json:"started_at,omitempty"`
	// Optional last time the entity was started
	FinishedAt string `protobuf:"bytes,12,opt,name=finished_at,json=finishedAt,proto3" json:"finished_at,omitempty"`
	// Required project name
	Project string `protobuf:"bytes,13,opt,name=project,proto3" json:"project,omitempty"`
	// Optional flag to tell if this entity is managed by the platform
	IsManaged string `protobuf:"bytes,14,opt,name=is_managed,json=isManaged,proto3" json:"is_managed,omitempty"`
	// Optional content of the entity's spec
	Spec string `protobuf:"bytes,15,opt,name=spec,proto3" json:"spec,omitempty"`
	// Optional backend value of this entity
	Backend string `protobuf:"bytes,16,opt,name=backend,proto3" json:"backend,omitempty"`
	// Optional framework name of this entity
	Framework string `protobuf:"bytes,17,opt,name=framework,proto3" json:"framework,omitempty"`
	// Optional latest status of this entity
	LastStatus string `protobuf:"bytes,18,opt,name=last_status,json=lastStatus,proto3" json:"last_status,omitempty"`
	// Optional Code reference
	CodeReference int64 `protobuf:"varint,19,opt,name=code_reference,json=codeReference,proto3" json:"code_reference,omitempty"`
	// Optional hardware resources requested by this entity
	Resources map[string]string `protobuf:"bytes,20,rep,name=resources,proto3" json:"resources,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Optional a readme text describing this entity
	Readme string `protobuf:"bytes,21,opt,name=readme,proto3" json:"readme,omitempty"`
	// Optional if this entity was bookmarked
	Bookmarked bool `protobuf:"varint,22,opt,name=bookmarked,proto3" json:"bookmarked,omitempty"`
	// Optional params of this entity
	Params map[string]string `protobuf:"bytes,23,rep,name=params,proto3" json:"params,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Optional run enivronment tracked
	RunEnv map[string]string `protobuf:"bytes,24,rep,name=run_env,json=runEnv,proto3" json:"run_env,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Optional build build name
	BuildBuild           string   `protobuf:"bytes,25,opt,name=build_build,json=buildBuild,proto3" json:"build_build,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Build) Reset()         { *m = Build{} }
func (m *Build) String() string { return proto.CompactTextString(m) }
func (*Build) ProtoMessage()    {}
func (*Build) Descriptor() ([]byte, []int) {
	return fileDescriptor_0f276a347e0551d9, []int{0}
}

func (m *Build) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Build.Unmarshal(m, b)
}
func (m *Build) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Build.Marshal(b, m, deterministic)
}
func (m *Build) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Build.Merge(m, src)
}
func (m *Build) XXX_Size() int {
	return xxx_messageInfo_Build.Size(m)
}
func (m *Build) XXX_DiscardUnknown() {
	xxx_messageInfo_Build.DiscardUnknown(m)
}

var xxx_messageInfo_Build proto.InternalMessageInfo

func (m *Build) GetId() int64 {
	if m != nil {
		return m.Id
	}
	return 0
}

func (m *Build) GetUuid() string {
	if m != nil {
		return m.Uuid
	}
	return ""
}

func (m *Build) GetUniqueName() string {
	if m != nil {
		return m.UniqueName
	}
	return ""
}

func (m *Build) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Build) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

func (m *Build) GetTags() []string {
	if m != nil {
		return m.Tags
	}
	return nil
}

func (m *Build) GetDeleted() bool {
	if m != nil {
		return m.Deleted
	}
	return false
}

func (m *Build) GetUser() string {
	if m != nil {
		return m.User
	}
	return ""
}

func (m *Build) GetCreatedAt() string {
	if m != nil {
		return m.CreatedAt
	}
	return ""
}

func (m *Build) GetUpdatedAt() string {
	if m != nil {
		return m.UpdatedAt
	}
	return ""
}

func (m *Build) GetStartedAt() string {
	if m != nil {
		return m.StartedAt
	}
	return ""
}

func (m *Build) GetFinishedAt() string {
	if m != nil {
		return m.FinishedAt
	}
	return ""
}

func (m *Build) GetProject() string {
	if m != nil {
		return m.Project
	}
	return ""
}

func (m *Build) GetIsManaged() string {
	if m != nil {
		return m.IsManaged
	}
	return ""
}

func (m *Build) GetSpec() string {
	if m != nil {
		return m.Spec
	}
	return ""
}

func (m *Build) GetBackend() string {
	if m != nil {
		return m.Backend
	}
	return ""
}

func (m *Build) GetFramework() string {
	if m != nil {
		return m.Framework
	}
	return ""
}

func (m *Build) GetLastStatus() string {
	if m != nil {
		return m.LastStatus
	}
	return ""
}

func (m *Build) GetCodeReference() int64 {
	if m != nil {
		return m.CodeReference
	}
	return 0
}

func (m *Build) GetResources() map[string]string {
	if m != nil {
		return m.Resources
	}
	return nil
}

func (m *Build) GetReadme() string {
	if m != nil {
		return m.Readme
	}
	return ""
}

func (m *Build) GetBookmarked() bool {
	if m != nil {
		return m.Bookmarked
	}
	return false
}

func (m *Build) GetParams() map[string]string {
	if m != nil {
		return m.Params
	}
	return nil
}

func (m *Build) GetRunEnv() map[string]string {
	if m != nil {
		return m.RunEnv
	}
	return nil
}

func (m *Build) GetBuildBuild() string {
	if m != nil {
		return m.BuildBuild
	}
	return ""
}

// Build specification
type BuildStatus struct {
	// Unique integer identifier
	Id int64 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	// UUID
	Uuid string `protobuf:"bytes,2,opt,name=uuid,proto3" json:"uuid,omitempty"`
	// Optional time when the entityt was created
	CreatedAt string `protobuf:"bytes,3,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	// Optional last time the entity was updated
	UpdatedAt string `protobuf:"bytes,4,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	// Optional status recorded
	Status string `protobuf:"bytes,5,opt,name=status,proto3" json:"status,omitempty"`
	// Optional status message
	Message              string   `protobuf:"bytes,6,opt,name=message,proto3" json:"message,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *BuildStatus) Reset()         { *m = BuildStatus{} }
func (m *BuildStatus) String() string { return proto.CompactTextString(m) }
func (*BuildStatus) ProtoMessage()    {}
func (*BuildStatus) Descriptor() ([]byte, []int) {
	return fileDescriptor_0f276a347e0551d9, []int{1}
}

func (m *BuildStatus) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_BuildStatus.Unmarshal(m, b)
}
func (m *BuildStatus) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_BuildStatus.Marshal(b, m, deterministic)
}
func (m *BuildStatus) XXX_Merge(src proto.Message) {
	xxx_messageInfo_BuildStatus.Merge(m, src)
}
func (m *BuildStatus) XXX_Size() int {
	return xxx_messageInfo_BuildStatus.Size(m)
}
func (m *BuildStatus) XXX_DiscardUnknown() {
	xxx_messageInfo_BuildStatus.DiscardUnknown(m)
}

var xxx_messageInfo_BuildStatus proto.InternalMessageInfo

func (m *BuildStatus) GetId() int64 {
	if m != nil {
		return m.Id
	}
	return 0
}

func (m *BuildStatus) GetUuid() string {
	if m != nil {
		return m.Uuid
	}
	return ""
}

func (m *BuildStatus) GetCreatedAt() string {
	if m != nil {
		return m.CreatedAt
	}
	return ""
}

func (m *BuildStatus) GetUpdatedAt() string {
	if m != nil {
		return m.UpdatedAt
	}
	return ""
}

func (m *BuildStatus) GetStatus() string {
	if m != nil {
		return m.Status
	}
	return ""
}

func (m *BuildStatus) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

// Request data to create/update build
type BuildBodyRequest struct {
	// Owner of the namespace
	Owner string `protobuf:"bytes,1,opt,name=owner,proto3" json:"owner,omitempty"`
	// Project where the experiement will be assigned
	Project string `protobuf:"bytes,2,opt,name=project,proto3" json:"project,omitempty"`
	// Build object
	Build                *Build   `protobuf:"bytes,3,opt,name=build,proto3" json:"build,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *BuildBodyRequest) Reset()         { *m = BuildBodyRequest{} }
func (m *BuildBodyRequest) String() string { return proto.CompactTextString(m) }
func (*BuildBodyRequest) ProtoMessage()    {}
func (*BuildBodyRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_0f276a347e0551d9, []int{2}
}

func (m *BuildBodyRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_BuildBodyRequest.Unmarshal(m, b)
}
func (m *BuildBodyRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_BuildBodyRequest.Marshal(b, m, deterministic)
}
func (m *BuildBodyRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_BuildBodyRequest.Merge(m, src)
}
func (m *BuildBodyRequest) XXX_Size() int {
	return xxx_messageInfo_BuildBodyRequest.Size(m)
}
func (m *BuildBodyRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_BuildBodyRequest.DiscardUnknown(m)
}

var xxx_messageInfo_BuildBodyRequest proto.InternalMessageInfo

func (m *BuildBodyRequest) GetOwner() string {
	if m != nil {
		return m.Owner
	}
	return ""
}

func (m *BuildBodyRequest) GetProject() string {
	if m != nil {
		return m.Project
	}
	return ""
}

func (m *BuildBodyRequest) GetBuild() *Build {
	if m != nil {
		return m.Build
	}
	return nil
}

// Contains list builds
type ListBuildsResponse struct {
	// Count of the entities
	Count int32 `protobuf:"varint,1,opt,name=count,proto3" json:"count,omitempty"`
	// List of all entities
	Results []*Build `protobuf:"bytes,2,rep,name=results,proto3" json:"results,omitempty"`
	// Previous page
	Previous string `protobuf:"bytes,3,opt,name=previous,proto3" json:"previous,omitempty"`
	// Next page
	Next                 string   `protobuf:"bytes,4,opt,name=next,proto3" json:"next,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListBuildsResponse) Reset()         { *m = ListBuildsResponse{} }
func (m *ListBuildsResponse) String() string { return proto.CompactTextString(m) }
func (*ListBuildsResponse) ProtoMessage()    {}
func (*ListBuildsResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_0f276a347e0551d9, []int{3}
}

func (m *ListBuildsResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListBuildsResponse.Unmarshal(m, b)
}
func (m *ListBuildsResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListBuildsResponse.Marshal(b, m, deterministic)
}
func (m *ListBuildsResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListBuildsResponse.Merge(m, src)
}
func (m *ListBuildsResponse) XXX_Size() int {
	return xxx_messageInfo_ListBuildsResponse.Size(m)
}
func (m *ListBuildsResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ListBuildsResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ListBuildsResponse proto.InternalMessageInfo

func (m *ListBuildsResponse) GetCount() int32 {
	if m != nil {
		return m.Count
	}
	return 0
}

func (m *ListBuildsResponse) GetResults() []*Build {
	if m != nil {
		return m.Results
	}
	return nil
}

func (m *ListBuildsResponse) GetPrevious() string {
	if m != nil {
		return m.Previous
	}
	return ""
}

func (m *ListBuildsResponse) GetNext() string {
	if m != nil {
		return m.Next
	}
	return ""
}

// Contains list builds
type ListBuildStatusesResponse struct {
	// Count of the entities
	Count int32 `protobuf:"varint,1,opt,name=count,proto3" json:"count,omitempty"`
	// List of all entities
	Results []*BuildStatus `protobuf:"bytes,2,rep,name=results,proto3" json:"results,omitempty"`
	// Previous page
	Previous string `protobuf:"bytes,3,opt,name=previous,proto3" json:"previous,omitempty"`
	// Next page
	Next                 string   `protobuf:"bytes,4,opt,name=next,proto3" json:"next,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListBuildStatusesResponse) Reset()         { *m = ListBuildStatusesResponse{} }
func (m *ListBuildStatusesResponse) String() string { return proto.CompactTextString(m) }
func (*ListBuildStatusesResponse) ProtoMessage()    {}
func (*ListBuildStatusesResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_0f276a347e0551d9, []int{4}
}

func (m *ListBuildStatusesResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListBuildStatusesResponse.Unmarshal(m, b)
}
func (m *ListBuildStatusesResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListBuildStatusesResponse.Marshal(b, m, deterministic)
}
func (m *ListBuildStatusesResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListBuildStatusesResponse.Merge(m, src)
}
func (m *ListBuildStatusesResponse) XXX_Size() int {
	return xxx_messageInfo_ListBuildStatusesResponse.Size(m)
}
func (m *ListBuildStatusesResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ListBuildStatusesResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ListBuildStatusesResponse proto.InternalMessageInfo

func (m *ListBuildStatusesResponse) GetCount() int32 {
	if m != nil {
		return m.Count
	}
	return 0
}

func (m *ListBuildStatusesResponse) GetResults() []*BuildStatus {
	if m != nil {
		return m.Results
	}
	return nil
}

func (m *ListBuildStatusesResponse) GetPrevious() string {
	if m != nil {
		return m.Previous
	}
	return ""
}

func (m *ListBuildStatusesResponse) GetNext() string {
	if m != nil {
		return m.Next
	}
	return ""
}

func init() {
	proto.RegisterType((*Build)(nil), "v1.Build")
	proto.RegisterMapType((map[string]string)(nil), "v1.Build.ParamsEntry")
	proto.RegisterMapType((map[string]string)(nil), "v1.Build.ResourcesEntry")
	proto.RegisterMapType((map[string]string)(nil), "v1.Build.RunEnvEntry")
	proto.RegisterType((*BuildStatus)(nil), "v1.BuildStatus")
	proto.RegisterType((*BuildBodyRequest)(nil), "v1.BuildBodyRequest")
	proto.RegisterType((*ListBuildsResponse)(nil), "v1.ListBuildsResponse")
	proto.RegisterType((*ListBuildStatusesResponse)(nil), "v1.ListBuildStatusesResponse")
}

func init() { proto.RegisterFile("v1/build.proto", fileDescriptor_0f276a347e0551d9) }

var fileDescriptor_0f276a347e0551d9 = []byte{
	// 735 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x9c, 0x54, 0xdd, 0x6e, 0x2a, 0x37,
	0x10, 0x16, 0x10, 0x20, 0x0c, 0x0d, 0x49, 0xdd, 0x24, 0x75, 0x50, 0xda, 0x20, 0xaa, 0x4a, 0x54,
	0x6a, 0x40, 0x49, 0xa5, 0xaa, 0xad, 0x7a, 0x93, 0x48, 0xb9, 0x6b, 0xab, 0x6a, 0xfb, 0x00, 0xc8,
	0xec, 0x0e, 0xdb, 0x2d, 0xac, 0xbd, 0xf1, 0x0f, 0x09, 0x57, 0x7d, 0x81, 0xbe, 0x44, 0x9f, 0xe1,
	0xbc, 0xe0, 0x91, 0xc7, 0x86, 0x90, 0x1c, 0xe9, 0x9c, 0x93, 0x73, 0x03, 0xfe, 0xbe, 0xcf, 0x33,
	0xf3, 0xcd, 0xda, 0x63, 0xe8, 0xad, 0xae, 0x26, 0x33, 0x57, 0x2c, 0xb3, 0x71, 0xa5, 0x95, 0x55,
	0xac, 0xbe, 0xba, 0xea, 0x9f, 0xe7, 0x4a, 0xe5, 0x4b, 0x9c, 0x88, 0xaa, 0x98, 0x08, 0x29, 0x95,
	0x15, 0xb6, 0x50, 0xd2, 0x84, 0x1d, 0xfd, 0xb3, 0xa8, 0x12, 0x9a, 0xb9, 0xf9, 0x44, 0xc8, 0x75,
	0x94, 0xbe, 0xa7, 0xbf, 0xf4, 0x32, 0x47, 0x79, 0x69, 0x1e, 0x44, 0x9e, 0xa3, 0x9e, 0xa8, 0x8a,
	0x82, 0xdf, 0x4d, 0x34, 0x7c, 0xd3, 0x86, 0xe6, 0xad, 0x2f, 0xcd, 0x7a, 0x50, 0x2f, 0x32, 0x5e,
	0x1b, 0xd4, 0x46, 0x8d, 0xa4, 0x5e, 0x64, 0x8c, 0xc1, 0x9e, 0x73, 0x45, 0xc6, 0xeb, 0x83, 0xda,
	0xa8, 0x93, 0xd0, 0x9a, 0x5d, 0x40, 0xd7, 0xc9, 0xe2, 0xde, 0xe1, 0x54, 0x8a, 0x12, 0x79, 0x83,
	0x24, 0x08, 0xd4, 0x1f, 0xa2, 0x44, 0x1f, 0x44, 0xca, 0x5e, 0x08, 0xf2, 0x6b, 0x36, 0x80, 0x6e,
	0x86, 0x26, 0xd5, 0x05, 0x99, 0xe0, 0x4d, 0x92, 0x76, 0x29, 0x1f, 0x65, 0x45, 0x6e, 0x78, 0x6b,
	0xd0, 0xf0, 0x51, 0x7e, 0xcd, 0x38, 0xb4, 0x33, 0x5c, 0xa2, 0xc5, 0x8c, 0xb7, 0x07, 0xb5, 0xd1,
	0x7e, 0xb2, 0x81, 0x64, 0xcc, 0xa0, 0xe6, 0xfb, 0xd1, 0x98, 0x41, 0xcd, 0xbe, 0x02, 0x48, 0x35,
	0x0a, 0x8b, 0xd9, 0x54, 0x58, 0xde, 0x21, 0xa5, 0x13, 0x99, 0x1b, 0xeb, 0x65, 0x57, 0x65, 0x1b,
	0x19, 0x82, 0x1c, 0x99, 0x20, 0x1b, 0x2b, 0x74, 0x94, 0xbb, 0x41, 0x8e, 0xcc, 0x8d, 0xf5, 0x5d,
	0xcf, 0x0b, 0x59, 0x98, 0xbf, 0x83, 0xfe, 0x59, 0xe8, 0x7a, 0x43, 0xdd, 0x58, 0xef, 0xb5, 0xd2,
	0xea, 0x1f, 0x4c, 0x2d, 0x3f, 0x20, 0x71, 0x03, 0x7d, 0xe6, 0xc2, 0x4c, 0x4b, 0x21, 0x45, 0x8e,
	0x19, 0xef, 0x85, 0xcc, 0x85, 0xf9, 0x3d, 0x10, 0xbe, 0x15, 0x53, 0x61, 0xca, 0x0f, 0x43, 0x2b,
	0x7e, 0xed, 0x93, 0xcd, 0x44, 0xba, 0x40, 0x99, 0xf1, 0xa3, 0x90, 0x2c, 0x42, 0x76, 0x0e, 0x9d,
	0xb9, 0x16, 0x25, 0x3e, 0x28, 0xbd, 0xe0, 0x9f, 0x87, 0x5c, 0x5b, 0xc2, 0xbb, 0x5c, 0x0a, 0x63,
	0xa7, 0xc6, 0x0a, 0xeb, 0x0c, 0x67, 0xc1, 0xa5, 0xa7, 0xfe, 0x22, 0x86, 0x7d, 0x0b, 0xbd, 0x54,
	0x65, 0x38, 0xd5, 0x38, 0x47, 0x8d, 0x32, 0x45, 0xfe, 0x05, 0x1d, 0xf6, 0x81, 0x67, 0x93, 0x0d,
	0xc9, 0x7e, 0x84, 0x8e, 0x46, 0xa3, 0x9c, 0x4e, 0xd1, 0xf0, 0xe3, 0x41, 0x63, 0xd4, 0xbd, 0xe6,
	0xe3, 0xd5, 0xd5, 0x98, 0x6e, 0xc9, 0x38, 0xd9, 0x48, 0x77, 0xd2, 0xea, 0x75, 0xf2, 0xb4, 0x95,
	0x9d, 0x42, 0x4b, 0xa3, 0xc8, 0x4a, 0xe4, 0x27, 0x54, 0x3a, 0x22, 0xf6, 0x35, 0xc0, 0x4c, 0xa9,
	0x45, 0x29, 0xf4, 0x02, 0x33, 0x7e, 0x4a, 0x67, 0xb9, 0xc3, 0xb0, 0x4b, 0x68, 0x55, 0x42, 0x8b,
	0xd2, 0xf0, 0x2f, 0xa9, 0xd8, 0xc9, 0x53, 0xb1, 0x3f, 0x89, 0x0f, 0x95, 0xe2, 0x26, 0x36, 0x86,
	0xb6, 0x76, 0x72, 0x8a, 0x72, 0xc5, 0xf9, 0xcb, 0xfd, 0x89, 0x93, 0x77, 0x72, 0x15, 0xf7, 0x6b,
	0x02, 0xfe, 0xb3, 0xd0, 0x68, 0x4d, 0xe9, 0x97, 0x9f, 0x85, 0xcf, 0x42, 0x80, 0x82, 0xfa, 0xbf,
	0x42, 0xef, 0x79, 0x53, 0xec, 0x08, 0x1a, 0x0b, 0x5c, 0xd3, 0x28, 0x74, 0x12, 0xbf, 0x64, 0xc7,
	0xd0, 0x5c, 0x89, 0xa5, 0xc3, 0x38, 0x0c, 0x01, 0xfc, 0x52, 0xff, 0xa9, 0xd6, 0xff, 0x19, 0xba,
	0x3b, 0x2e, 0x5f, 0x1b, 0xba, 0x63, 0xf8, 0x35, 0xa1, 0xc3, 0xff, 0x6b, 0xd0, 0x25, 0xf7, 0xf1,
	0x68, 0x3f, 0x66, 0x76, 0x9f, 0x8f, 0x48, 0xe3, 0xfd, 0x23, 0xb2, 0xf7, 0x72, 0x44, 0x4e, 0xa1,
	0x15, 0x2f, 0x56, 0x98, 0xdf, 0x88, 0xfc, 0x6d, 0x2d, 0xd1, 0x18, 0x91, 0x23, 0x6f, 0x85, 0xdb,
	0x1a, 0xe1, 0x30, 0x85, 0x23, 0xb2, 0x78, 0xab, 0xb2, 0x75, 0x82, 0xf7, 0x0e, 0x8d, 0xf5, 0x1d,
	0xa9, 0x07, 0x89, 0x3a, 0x76, 0x19, 0xc0, 0xee, 0xf8, 0xd4, 0x9f, 0x8f, 0xcf, 0x05, 0x34, 0xc3,
	0xb1, 0x79, 0xbb, 0xdd, 0xeb, 0xce, 0xf6, 0xa8, 0x93, 0xc0, 0x0f, 0xff, 0x05, 0xf6, 0x5b, 0x61,
	0x2c, 0x71, 0x26, 0x41, 0x53, 0x29, 0x69, 0xd0, 0x97, 0x49, 0x95, 0x93, 0x96, 0xca, 0x34, 0x93,
	0x00, 0xd8, 0x37, 0xd0, 0xd6, 0x68, 0xdc, 0xd2, 0x1a, 0x5e, 0xa7, 0x9b, 0xb3, 0x93, 0x6e, 0xa3,
	0xb0, 0x3e, 0xec, 0x57, 0x1a, 0x57, 0x85, 0x72, 0x26, 0x7e, 0xa3, 0x2d, 0xa6, 0xc7, 0x0d, 0x1f,
	0xed, 0xf6, 0x71, 0xc3, 0x47, 0x3b, 0xfc, 0xaf, 0x06, 0x67, 0x5b, 0x07, 0xe1, 0x34, 0xf0, 0x43,
	0x46, 0xbe, 0x7b, 0x69, 0xe4, 0x70, 0x6b, 0x24, 0x64, 0xf8, 0x64, 0x3b, 0xb3, 0x16, 0xbd, 0xea,
	0x3f, 0xbc, 0x0d, 0x00, 0x00, 0xff, 0xff, 0xc1, 0x3e, 0x4a, 0x96, 0x52, 0x06, 0x00, 0x00,
}
