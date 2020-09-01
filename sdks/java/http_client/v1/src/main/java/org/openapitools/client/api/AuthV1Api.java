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

/*
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


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.RuntimeError;
import org.openapitools.client.model.V1Auth;
import org.openapitools.client.model.V1Credentials;
import org.openapitools.client.model.V1PasswordChange;
import org.openapitools.client.model.V1UserEmail;
import org.openapitools.client.model.V1UserSingup;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AuthV1Api {
    private ApiClient localVarApiClient;

    public AuthV1Api() {
        this(Configuration.getDefaultApiClient());
    }

    public AuthV1Api(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    /**
     * Build call for changePassword
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changePasswordCall(V1PasswordChange body, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/v1/auth/change-password";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] { "ApiKey" };
        return localVarApiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call changePasswordValidateBeforeCall(V1PasswordChange body, final ApiCallback _callback) throws ApiException {
        
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling changePassword(Async)");
        }
        

        okhttp3.Call localVarCall = changePasswordCall(body, _callback);
        return localVarCall;

    }

    /**
     * Change password
     * 
     * @param body  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public void changePassword(V1PasswordChange body) throws ApiException {
        changePasswordWithHttpInfo(body);
    }

    /**
     * Change password
     * 
     * @param body  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changePasswordWithHttpInfo(V1PasswordChange body) throws ApiException {
        okhttp3.Call localVarCall = changePasswordValidateBeforeCall(body, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Change password (asynchronously)
     * 
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changePasswordAsync(V1PasswordChange body, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changePasswordValidateBeforeCall(body, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for login
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loginCall(V1Credentials body, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/v1/auth/token";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] { "ApiKey" };
        return localVarApiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loginValidateBeforeCall(V1Credentials body, final ApiCallback _callback) throws ApiException {
        
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling login(Async)");
        }
        

        okhttp3.Call localVarCall = loginCall(body, _callback);
        return localVarCall;

    }

    /**
     * Login
     * 
     * @param body  (required)
     * @return V1Auth
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public V1Auth login(V1Credentials body) throws ApiException {
        ApiResponse<V1Auth> localVarResp = loginWithHttpInfo(body);
        return localVarResp.getData();
    }

    /**
     * Login
     * 
     * @param body  (required)
     * @return ApiResponse&lt;V1Auth&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<V1Auth> loginWithHttpInfo(V1Credentials body) throws ApiException {
        okhttp3.Call localVarCall = loginValidateBeforeCall(body, null);
        Type localVarReturnType = new TypeToken<V1Auth>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Login (asynchronously)
     * 
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loginAsync(V1Credentials body, final ApiCallback<V1Auth> _callback) throws ApiException {

        okhttp3.Call localVarCall = loginValidateBeforeCall(body, _callback);
        Type localVarReturnType = new TypeToken<V1Auth>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resetPassword
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetPasswordCall(V1UserEmail body, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/v1/auth/reset-password";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] { "ApiKey" };
        return localVarApiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resetPasswordValidateBeforeCall(V1UserEmail body, final ApiCallback _callback) throws ApiException {
        
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling resetPassword(Async)");
        }
        

        okhttp3.Call localVarCall = resetPasswordCall(body, _callback);
        return localVarCall;

    }

    /**
     * Reset password
     * 
     * @param body  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public void resetPassword(V1UserEmail body) throws ApiException {
        resetPasswordWithHttpInfo(body);
    }

    /**
     * Reset password
     * 
     * @param body  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> resetPasswordWithHttpInfo(V1UserEmail body) throws ApiException {
        okhttp3.Call localVarCall = resetPasswordValidateBeforeCall(body, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Reset password (asynchronously)
     * 
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetPasswordAsync(V1UserEmail body, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = resetPasswordValidateBeforeCall(body, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for resetPasswordConfirm
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetPasswordConfirmCall(V1PasswordChange body, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/v1/auth/reset-password-confirm";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] { "ApiKey" };
        return localVarApiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resetPasswordConfirmValidateBeforeCall(V1PasswordChange body, final ApiCallback _callback) throws ApiException {
        
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling resetPasswordConfirm(Async)");
        }
        

        okhttp3.Call localVarCall = resetPasswordConfirmCall(body, _callback);
        return localVarCall;

    }

    /**
     * Reset password confirm
     * 
     * @param body  (required)
     * @return V1Auth
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public V1Auth resetPasswordConfirm(V1PasswordChange body) throws ApiException {
        ApiResponse<V1Auth> localVarResp = resetPasswordConfirmWithHttpInfo(body);
        return localVarResp.getData();
    }

    /**
     * Reset password confirm
     * 
     * @param body  (required)
     * @return ApiResponse&lt;V1Auth&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<V1Auth> resetPasswordConfirmWithHttpInfo(V1PasswordChange body) throws ApiException {
        okhttp3.Call localVarCall = resetPasswordConfirmValidateBeforeCall(body, null);
        Type localVarReturnType = new TypeToken<V1Auth>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reset password confirm (asynchronously)
     * 
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetPasswordConfirmAsync(V1PasswordChange body, final ApiCallback<V1Auth> _callback) throws ApiException {

        okhttp3.Call localVarCall = resetPasswordConfirmValidateBeforeCall(body, _callback);
        Type localVarReturnType = new TypeToken<V1Auth>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for signup
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call signupCall(V1UserSingup body, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/v1/auth/signup";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] { "ApiKey" };
        return localVarApiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call signupValidateBeforeCall(V1UserSingup body, final ApiCallback _callback) throws ApiException {
        
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling signup(Async)");
        }
        

        okhttp3.Call localVarCall = signupCall(body, _callback);
        return localVarCall;

    }

    /**
     * Signup
     * 
     * @param body  (required)
     * @return V1Auth
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public V1Auth signup(V1UserSingup body) throws ApiException {
        ApiResponse<V1Auth> localVarResp = signupWithHttpInfo(body);
        return localVarResp.getData();
    }

    /**
     * Signup
     * 
     * @param body  (required)
     * @return ApiResponse&lt;V1Auth&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<V1Auth> signupWithHttpInfo(V1UserSingup body) throws ApiException {
        okhttp3.Call localVarCall = signupValidateBeforeCall(body, null);
        Type localVarReturnType = new TypeToken<V1Auth>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Signup (asynchronously)
     * 
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A successful response. </td><td>  -  </td></tr>
        <tr><td> 204 </td><td> No content. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> You don&#39;t have permission to access the resource. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource does not exist. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> An unexpected error response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call signupAsync(V1UserSingup body, final ApiCallback<V1Auth> _callback) throws ApiException {

        okhttp3.Call localVarCall = signupValidateBeforeCall(body, _callback);
        Type localVarReturnType = new TypeToken<V1Auth>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
