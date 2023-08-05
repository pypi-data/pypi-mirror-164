# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailslurp_client.api_client import ApiClient
from mailslurp_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EmailVerificationControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_validation_requests(self, **kwargs):  # noqa: E501
        """Validate a list of email addresses. Per unit billing. See your plan for pricing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_validation_requests(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Optional page index in list pagination
        :param int size: Optional page size for paginated result list.
        :param str sort: Optional createdAt sort direction ASC or DESC
        :param str search_filter: Optional search filter
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param bool is_valid: Filter where email is valid is true or false
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PageEmailValidationRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_validation_requests_with_http_info(**kwargs)  # noqa: E501

    def get_validation_requests_with_http_info(self, **kwargs):  # noqa: E501
        """Validate a list of email addresses. Per unit billing. See your plan for pricing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_validation_requests_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Optional page index in list pagination
        :param int size: Optional page size for paginated result list.
        :param str sort: Optional createdAt sort direction ASC or DESC
        :param str search_filter: Optional search filter
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param bool is_valid: Filter where email is valid is true or false
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PageEmailValidationRequest, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'page',
            'size',
            'sort',
            'search_filter',
            'since',
            'before',
            'is_valid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_validation_requests" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] > 9223372036854775807:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_validation_requests`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `get_validation_requests`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'size' in local_var_params and local_var_params['size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `size` when calling `get_validation_requests`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'size' in local_var_params and local_var_params['size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `size` when calling `get_validation_requests`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'size' in local_var_params and local_var_params['size'] is not None:  # noqa: E501
            query_params.append(('size', local_var_params['size']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'search_filter' in local_var_params and local_var_params['search_filter'] is not None:  # noqa: E501
            query_params.append(('searchFilter', local_var_params['search_filter']))  # noqa: E501
        if 'since' in local_var_params and local_var_params['since'] is not None:  # noqa: E501
            query_params.append(('since', local_var_params['since']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501
        if 'is_valid' in local_var_params and local_var_params['is_valid'] is not None:  # noqa: E501
            query_params.append(('isValid', local_var_params['is_valid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/email-verification/validation-requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageEmailValidationRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_email_address_list(self, validate_email_address_list_options, **kwargs):  # noqa: E501
        """Validate a list of email addresses. Per unit billing. See your plan for pricing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_email_address_list(validate_email_address_list_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ValidateEmailAddressListOptions validate_email_address_list_options: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ValidateEmailAddressListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.validate_email_address_list_with_http_info(validate_email_address_list_options, **kwargs)  # noqa: E501

    def validate_email_address_list_with_http_info(self, validate_email_address_list_options, **kwargs):  # noqa: E501
        """Validate a list of email addresses. Per unit billing. See your plan for pricing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_email_address_list_with_http_info(validate_email_address_list_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ValidateEmailAddressListOptions validate_email_address_list_options: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ValidateEmailAddressListResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'validate_email_address_list_options'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_email_address_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'validate_email_address_list_options' is set
        if self.api_client.client_side_validation and ('validate_email_address_list_options' not in local_var_params or  # noqa: E501
                                                        local_var_params['validate_email_address_list_options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `validate_email_address_list_options` when calling `validate_email_address_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'validate_email_address_list_options' in local_var_params:
            body_params = local_var_params['validate_email_address_list_options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/email-verification/email-address-list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateEmailAddressListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
