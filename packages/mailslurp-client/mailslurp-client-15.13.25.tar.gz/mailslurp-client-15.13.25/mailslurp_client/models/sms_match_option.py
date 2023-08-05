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


class SmsMatchOption(object):
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
        'field': 'str',
        'should': 'str',
        'value': 'str'
    }

    attribute_map = {
        'field': 'field',
        'should': 'should',
        'value': 'value'
    }

    def __init__(self, field=None, should=None, value=None, local_vars_configuration=None):  # noqa: E501
        """SmsMatchOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._should = None
        self._value = None
        self.discriminator = None

        self.field = field
        self.should = should
        self.value = value

    @property
    def field(self):
        """Gets the field of this SmsMatchOption.  # noqa: E501

        Fields of an SMS object that can be used to filter results  # noqa: E501

        :return: The field of this SmsMatchOption.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SmsMatchOption.

        Fields of an SMS object that can be used to filter results  # noqa: E501

        :param field: The field of this SmsMatchOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        allowed_values = ["BODY", "FROM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `field` ({0}), must be one of {1}"  # noqa: E501
                .format(field, allowed_values)
            )

        self._field = field

    @property
    def should(self):
        """Gets the should of this SmsMatchOption.  # noqa: E501

        How the value of the email field specified should be compared to the value given in the match options.  # noqa: E501

        :return: The should of this SmsMatchOption.  # noqa: E501
        :rtype: str
        """
        return self._should

    @should.setter
    def should(self, should):
        """Sets the should of this SmsMatchOption.

        How the value of the email field specified should be compared to the value given in the match options.  # noqa: E501

        :param should: The should of this SmsMatchOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and should is None:  # noqa: E501
            raise ValueError("Invalid value for `should`, must not be `None`")  # noqa: E501
        allowed_values = ["CONTAIN", "EQUAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and should not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `should` ({0}), must be one of {1}"  # noqa: E501
                .format(should, allowed_values)
            )

        self._should = should

    @property
    def value(self):
        """Gets the value of this SmsMatchOption.  # noqa: E501

        The value you wish to compare with the value of the field specified using the `should` value passed. For example `BODY` should `CONTAIN` a value passed.  # noqa: E501

        :return: The value of this SmsMatchOption.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SmsMatchOption.

        The value you wish to compare with the value of the field specified using the `should` value passed. For example `BODY` should `CONTAIN` a value passed.  # noqa: E501

        :param value: The value of this SmsMatchOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, SmsMatchOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmsMatchOption):
            return True

        return self.to_dict() != other.to_dict()
