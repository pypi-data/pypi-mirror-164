# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class EmailVerificationResult(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'domain_name': 'str',
        'port': 'int',
        'email_address': 'str',
        'is_valid': 'bool',
        'error': 'str'
    }

    attribute_map = {
        'domain_name': 'domainName',
        'port': 'port',
        'email_address': 'emailAddress',
        'is_valid': 'isValid',
        'error': 'error'
    }

    def __init__(self, domain_name=None, port=None, email_address=None, is_valid=None, error=None, local_vars_configuration=None):  # noqa: E501
        """EmailVerificationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain_name = None
        self._port = None
        self._email_address = None
        self._is_valid = None
        self._error = None
        self.discriminator = None

        self.domain_name = domain_name
        self.port = port
        self.email_address = email_address
        self.is_valid = is_valid
        if error is not None:
            self.error = error

    @property
    def domain_name(self):
        """Gets the domain_name of this EmailVerificationResult.  # noqa: E501


        :return: The domain_name of this EmailVerificationResult.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this EmailVerificationResult.


        :param domain_name: The domain_name of this EmailVerificationResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain_name is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_name`, must not be `None`")  # noqa: E501

        self._domain_name = domain_name

    @property
    def port(self):
        """Gets the port of this EmailVerificationResult.  # noqa: E501


        :return: The port of this EmailVerificationResult.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this EmailVerificationResult.


        :param port: The port of this EmailVerificationResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def email_address(self):
        """Gets the email_address of this EmailVerificationResult.  # noqa: E501


        :return: The email_address of this EmailVerificationResult.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this EmailVerificationResult.


        :param email_address: The email_address of this EmailVerificationResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def is_valid(self):
        """Gets the is_valid of this EmailVerificationResult.  # noqa: E501


        :return: The is_valid of this EmailVerificationResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this EmailVerificationResult.


        :param is_valid: The is_valid of this EmailVerificationResult.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_valid is None:  # noqa: E501
            raise ValueError("Invalid value for `is_valid`, must not be `None`")  # noqa: E501

        self._is_valid = is_valid

    @property
    def error(self):
        """Gets the error of this EmailVerificationResult.  # noqa: E501


        :return: The error of this EmailVerificationResult.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EmailVerificationResult.


        :param error: The error of this EmailVerificationResult.  # noqa: E501
        :type: str
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmailVerificationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailVerificationResult):
            return True

        return self.to_dict() != other.to_dict()
