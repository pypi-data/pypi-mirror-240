from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_logging.api_client import ApiClient
from ionoscloud_logging.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PipelinesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pipelines_delete(self, pipeline_id, **kwargs):  # noqa: E501
        """Delete a pipeline  # noqa: E501

        Delete a logging pipeline.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_delete(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Pipeline
        """
        kwargs['_return_http_data_only'] = True
        return self.pipelines_delete_with_http_info(pipeline_id, **kwargs)  # noqa: E501

    def pipelines_delete_with_http_info(self, pipeline_id, **kwargs):  # noqa: E501
        """Delete a pipeline  # noqa: E501

        Delete a logging pipeline.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_delete_with_http_info(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pipeline_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pipelines_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `pipelines_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'Pipeline'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/pipelines/{pipelineId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pipelines_find_by_id(self, pipeline_id, **kwargs):  # noqa: E501
        """Fetch a pipeline  # noqa: E501

        You can retrieve a pipeline by using its ID. This value can be found in the response body when a pipeline is created or when you GET a list of pipelines.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_find_by_id(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Pipeline
        """
        kwargs['_return_http_data_only'] = True
        return self.pipelines_find_by_id_with_http_info(pipeline_id, **kwargs)  # noqa: E501

    def pipelines_find_by_id_with_http_info(self, pipeline_id, **kwargs):  # noqa: E501
        """Fetch a pipeline  # noqa: E501

        You can retrieve a pipeline by using its ID. This value can be found in the response body when a pipeline is created or when you GET a list of pipelines.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_find_by_id_with_http_info(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pipeline_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pipelines_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `pipelines_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'Pipeline'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/pipelines/{pipelineId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pipelines_get(self, **kwargs):  # noqa: E501
        """List pipelines  # noqa: E501

        Retrieves a list of all logging pipelines.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_get(async_req=True)
        >>> result = thread.get()

        :param limit: the maximum number of elements to return (use together with offset for pagination). Default to 100
        :type limit: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with limit for pagination). Default to 0
        :type offset: int
        :param order_by: Sorts the results alphanumerically in ascending order based on the specified property
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PipelineListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.pipelines_get_with_http_info(**kwargs)  # noqa: E501

    def pipelines_get_with_http_info(self, **kwargs):  # noqa: E501
        """List pipelines  # noqa: E501

        Retrieves a list of all logging pipelines.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: the maximum number of elements to return (use together with offset for pagination). Default to 100
        :type limit: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with limit for pagination). Default to 0
        :type offset: int
        :param order_by: Sorts the results alphanumerically in ascending order based on the specified property
        :type order_by: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PipelineListResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset',
            'order_by'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pipelines_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `pipelines_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `pipelines_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'PipelineListResponse'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/pipelines', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pipelines_key_post(self, pipeline_id, **kwargs):  # noqa: E501
        """Renews the key of a Pipeline  # noqa: E501

        Generates a new key for a pipeline invalidating the old one. The key is used for authentication when sending logs (Shared_Key parameter in the context of fluent-bit).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_key_post(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PipelinesKeyPost200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.pipelines_key_post_with_http_info(pipeline_id, **kwargs)  # noqa: E501

    def pipelines_key_post_with_http_info(self, pipeline_id, **kwargs):  # noqa: E501
        """Renews the key of a Pipeline  # noqa: E501

        Generates a new key for a pipeline invalidating the old one. The key is used for authentication when sending logs (Shared_Key parameter in the context of fluent-bit).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_key_post_with_http_info(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PipelinesKeyPost200Response, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pipeline_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pipelines_key_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `pipelines_key_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'PipelinesKeyPost200Response'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/pipelines/{pipelineId}/key', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pipelines_patch(self, pipeline_id, pipeline, **kwargs):  # noqa: E501
        """Patch a pipeline  # noqa: E501

        Patch attributes of a logging pipeline.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_patch(pipeline_id, pipeline, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param pipeline: The modified pipeline. (required)
        :type pipeline: PipelinePatch
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Pipeline
        """
        kwargs['_return_http_data_only'] = True
        return self.pipelines_patch_with_http_info(pipeline_id, pipeline, **kwargs)  # noqa: E501

    def pipelines_patch_with_http_info(self, pipeline_id, pipeline, **kwargs):  # noqa: E501
        """Patch a pipeline  # noqa: E501

        Patch attributes of a logging pipeline.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_patch_with_http_info(pipeline_id, pipeline, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: The unique ID of the pipeline (required)
        :type pipeline_id: str
        :param pipeline: The modified pipeline. (required)
        :type pipeline: PipelinePatch
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pipeline_id',
            'pipeline'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pipelines_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `pipelines_patch`")  # noqa: E501
        # verify the required parameter 'pipeline' is set
        if self.api_client.client_side_validation and ('pipeline' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline` when calling `pipelines_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pipeline' in local_var_params:
            body_params = local_var_params['pipeline']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'Pipeline'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/pipelines/{pipelineId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def pipelines_post(self, pipeline, **kwargs):  # noqa: E501
        """Create a pipeline  # noqa: E501

        Creates a new logging pipeline.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_post(pipeline, async_req=True)
        >>> result = thread.get()

        :param pipeline: The pipeline to be created. (required)
        :type pipeline: PipelineCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Pipeline
        """
        kwargs['_return_http_data_only'] = True
        return self.pipelines_post_with_http_info(pipeline, **kwargs)  # noqa: E501

    def pipelines_post_with_http_info(self, pipeline, **kwargs):  # noqa: E501
        """Create a pipeline  # noqa: E501

        Creates a new logging pipeline.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pipelines_post_with_http_info(pipeline, async_req=True)
        >>> result = thread.get()

        :param pipeline: The pipeline to be created. (required)
        :type pipeline: PipelineCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pipeline'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pipelines_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'pipeline' is set
        if self.api_client.client_side_validation and ('pipeline' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline` when calling `pipelines_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pipeline' in local_var_params:
            body_params = local_var_params['pipeline']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'Pipeline'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/pipelines', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
