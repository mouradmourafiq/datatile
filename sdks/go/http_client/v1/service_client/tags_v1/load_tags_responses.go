// Copyright 2018-2021 Polyaxon, Inc.
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

// Code generated by go-swagger; DO NOT EDIT.

package tags_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// LoadTagsReader is a Reader for the LoadTags structure.
type LoadTagsReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *LoadTagsReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewLoadTagsOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 204:
		result := NewLoadTagsNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewLoadTagsForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewLoadTagsNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	default:
		result := NewLoadTagsDefault(response.Code())
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		if response.Code()/100 == 2 {
			return result, nil
		}
		return nil, result
	}
}

// NewLoadTagsOK creates a LoadTagsOK with default headers values
func NewLoadTagsOK() *LoadTagsOK {
	return &LoadTagsOK{}
}

/* LoadTagsOK describes a response with status code 200, with default header values.

A successful response.
*/
type LoadTagsOK struct {
	Payload interface{}
}

func (o *LoadTagsOK) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/tags/load][%d] loadTagsOK  %+v", 200, o.Payload)
}
func (o *LoadTagsOK) GetPayload() interface{} {
	return o.Payload
}

func (o *LoadTagsOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewLoadTagsNoContent creates a LoadTagsNoContent with default headers values
func NewLoadTagsNoContent() *LoadTagsNoContent {
	return &LoadTagsNoContent{}
}

/* LoadTagsNoContent describes a response with status code 204, with default header values.

No content.
*/
type LoadTagsNoContent struct {
	Payload interface{}
}

func (o *LoadTagsNoContent) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/tags/load][%d] loadTagsNoContent  %+v", 204, o.Payload)
}
func (o *LoadTagsNoContent) GetPayload() interface{} {
	return o.Payload
}

func (o *LoadTagsNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewLoadTagsForbidden creates a LoadTagsForbidden with default headers values
func NewLoadTagsForbidden() *LoadTagsForbidden {
	return &LoadTagsForbidden{}
}

/* LoadTagsForbidden describes a response with status code 403, with default header values.

You don't have permission to access the resource.
*/
type LoadTagsForbidden struct {
	Payload interface{}
}

func (o *LoadTagsForbidden) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/tags/load][%d] loadTagsForbidden  %+v", 403, o.Payload)
}
func (o *LoadTagsForbidden) GetPayload() interface{} {
	return o.Payload
}

func (o *LoadTagsForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewLoadTagsNotFound creates a LoadTagsNotFound with default headers values
func NewLoadTagsNotFound() *LoadTagsNotFound {
	return &LoadTagsNotFound{}
}

/* LoadTagsNotFound describes a response with status code 404, with default header values.

Resource does not exist.
*/
type LoadTagsNotFound struct {
	Payload interface{}
}

func (o *LoadTagsNotFound) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/tags/load][%d] loadTagsNotFound  %+v", 404, o.Payload)
}
func (o *LoadTagsNotFound) GetPayload() interface{} {
	return o.Payload
}

func (o *LoadTagsNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewLoadTagsDefault creates a LoadTagsDefault with default headers values
func NewLoadTagsDefault(code int) *LoadTagsDefault {
	return &LoadTagsDefault{
		_statusCode: code,
	}
}

/* LoadTagsDefault describes a response with status code -1, with default header values.

An unexpected error response.
*/
type LoadTagsDefault struct {
	_statusCode int

	Payload *service_model.RuntimeError
}

// Code gets the status code for the load tags default response
func (o *LoadTagsDefault) Code() int {
	return o._statusCode
}

func (o *LoadTagsDefault) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/tags/load][%d] LoadTags default  %+v", o._statusCode, o.Payload)
}
func (o *LoadTagsDefault) GetPayload() *service_model.RuntimeError {
	return o.Payload
}

func (o *LoadTagsDefault) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.RuntimeError)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}
