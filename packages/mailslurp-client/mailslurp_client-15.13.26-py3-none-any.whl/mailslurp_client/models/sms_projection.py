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


class SmsProjection(object):
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
        'id': 'str',
        'body': 'str',
        'user_id': 'str',
        'phone_number': 'str',
        'created_at': 'datetime',
        'from_number': 'str',
        'read': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'body': 'body',
        'user_id': 'userId',
        'phone_number': 'phoneNumber',
        'created_at': 'createdAt',
        'from_number': 'fromNumber',
        'read': 'read'
    }

    def __init__(self, id=None, body=None, user_id=None, phone_number=None, created_at=None, from_number=None, read=None, local_vars_configuration=None):  # noqa: E501
        """SmsProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._body = None
        self._user_id = None
        self._phone_number = None
        self._created_at = None
        self._from_number = None
        self._read = None
        self.discriminator = None

        self.id = id
        self.body = body
        self.user_id = user_id
        self.phone_number = phone_number
        self.created_at = created_at
        self.from_number = from_number
        self.read = read

    @property
    def id(self):
        """Gets the id of this SmsProjection.  # noqa: E501


        :return: The id of this SmsProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmsProjection.


        :param id: The id of this SmsProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def body(self):
        """Gets the body of this SmsProjection.  # noqa: E501


        :return: The body of this SmsProjection.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SmsProjection.


        :param body: The body of this SmsProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def user_id(self):
        """Gets the user_id of this SmsProjection.  # noqa: E501


        :return: The user_id of this SmsProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SmsProjection.


        :param user_id: The user_id of this SmsProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def phone_number(self):
        """Gets the phone_number of this SmsProjection.  # noqa: E501


        :return: The phone_number of this SmsProjection.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SmsProjection.


        :param phone_number: The phone_number of this SmsProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def created_at(self):
        """Gets the created_at of this SmsProjection.  # noqa: E501


        :return: The created_at of this SmsProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SmsProjection.


        :param created_at: The created_at of this SmsProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def from_number(self):
        """Gets the from_number of this SmsProjection.  # noqa: E501


        :return: The from_number of this SmsProjection.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this SmsProjection.


        :param from_number: The from_number of this SmsProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and from_number is None:  # noqa: E501
            raise ValueError("Invalid value for `from_number`, must not be `None`")  # noqa: E501

        self._from_number = from_number

    @property
    def read(self):
        """Gets the read of this SmsProjection.  # noqa: E501


        :return: The read of this SmsProjection.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this SmsProjection.


        :param read: The read of this SmsProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

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
        if not isinstance(other, SmsProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmsProjection):
            return True

        return self.to_dict() != other.to_dict()
