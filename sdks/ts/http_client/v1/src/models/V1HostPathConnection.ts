// Copyright 2018-2020 Polyaxon, Inc.
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

/* tslint:disable */
/* eslint-disable */
/**
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.1.8
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface V1HostPathConnection
 */
export interface V1HostPathConnection {
    /**
     * 
     * @type {string}
     * @memberof V1HostPathConnection
     */
    host_path?: string;
    /**
     * 
     * @type {string}
     * @memberof V1HostPathConnection
     */
    mount_path?: string;
    /**
     * 
     * @type {boolean}
     * @memberof V1HostPathConnection
     */
    read_only?: boolean;
    /**
     * 
     * @type {object}
     * @memberof V1HostPathConnection
     */
    kind?: object;
}

export function V1HostPathConnectionFromJSON(json: any): V1HostPathConnection {
    return V1HostPathConnectionFromJSONTyped(json, false);
}

export function V1HostPathConnectionFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1HostPathConnection {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'host_path': !exists(json, 'host_path') ? undefined : json['host_path'],
        'mount_path': !exists(json, 'mount_path') ? undefined : json['mount_path'],
        'read_only': !exists(json, 'read_only') ? undefined : json['read_only'],
        'kind': !exists(json, 'kind') ? undefined : json['kind'],
    };
}

export function V1HostPathConnectionToJSON(value?: V1HostPathConnection | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'host_path': value.host_path,
        'mount_path': value.mount_path,
        'read_only': value.read_only,
        'kind': value.kind,
    };
}


