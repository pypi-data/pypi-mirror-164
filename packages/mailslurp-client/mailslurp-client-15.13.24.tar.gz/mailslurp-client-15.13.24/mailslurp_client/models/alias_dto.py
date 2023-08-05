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


class AliasDto(object):
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
        'email_address': 'str',
        'masked_email_address': 'str',
        'user_id': 'str',
        'inbox_id': 'str',
        'name': 'str',
        'use_threads': 'bool',
        'is_verified': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'email_address': 'emailAddress',
        'masked_email_address': 'maskedEmailAddress',
        'user_id': 'userId',
        'inbox_id': 'inboxId',
        'name': 'name',
        'use_threads': 'useThreads',
        'is_verified': 'isVerified',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, email_address=None, masked_email_address=None, user_id=None, inbox_id=None, name=None, use_threads=None, is_verified=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """AliasDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email_address = None
        self._masked_email_address = None
        self._user_id = None
        self._inbox_id = None
        self._name = None
        self._use_threads = None
        self._is_verified = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.email_address = email_address
        if masked_email_address is not None:
            self.masked_email_address = masked_email_address
        self.user_id = user_id
        self.inbox_id = inbox_id
        if name is not None:
            self.name = name
        if use_threads is not None:
            self.use_threads = use_threads
        self.is_verified = is_verified
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this AliasDto.  # noqa: E501


        :return: The id of this AliasDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AliasDto.


        :param id: The id of this AliasDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_address(self):
        """Gets the email_address of this AliasDto.  # noqa: E501

        The alias's email address for receiving email  # noqa: E501

        :return: The email_address of this AliasDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AliasDto.

        The alias's email address for receiving email  # noqa: E501

        :param email_address: The email_address of this AliasDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def masked_email_address(self):
        """Gets the masked_email_address of this AliasDto.  # noqa: E501

        The underlying email address that is hidden and will received forwarded email  # noqa: E501

        :return: The masked_email_address of this AliasDto.  # noqa: E501
        :rtype: str
        """
        return self._masked_email_address

    @masked_email_address.setter
    def masked_email_address(self, masked_email_address):
        """Sets the masked_email_address of this AliasDto.

        The underlying email address that is hidden and will received forwarded email  # noqa: E501

        :param masked_email_address: The masked_email_address of this AliasDto.  # noqa: E501
        :type: str
        """

        self._masked_email_address = masked_email_address

    @property
    def user_id(self):
        """Gets the user_id of this AliasDto.  # noqa: E501


        :return: The user_id of this AliasDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AliasDto.


        :param user_id: The user_id of this AliasDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this AliasDto.  # noqa: E501

        Inbox that is associated with the alias  # noqa: E501

        :return: The inbox_id of this AliasDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this AliasDto.

        Inbox that is associated with the alias  # noqa: E501

        :param inbox_id: The inbox_id of this AliasDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def name(self):
        """Gets the name of this AliasDto.  # noqa: E501


        :return: The name of this AliasDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AliasDto.


        :param name: The name of this AliasDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def use_threads(self):
        """Gets the use_threads of this AliasDto.  # noqa: E501

        If alias will generate response threads or not when email are received by it  # noqa: E501

        :return: The use_threads of this AliasDto.  # noqa: E501
        :rtype: bool
        """
        return self._use_threads

    @use_threads.setter
    def use_threads(self, use_threads):
        """Sets the use_threads of this AliasDto.

        If alias will generate response threads or not when email are received by it  # noqa: E501

        :param use_threads: The use_threads of this AliasDto.  # noqa: E501
        :type: bool
        """

        self._use_threads = use_threads

    @property
    def is_verified(self):
        """Gets the is_verified of this AliasDto.  # noqa: E501

        Has the alias been verified. You must verify an alias if the masked email address has not yet been verified by your account  # noqa: E501

        :return: The is_verified of this AliasDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this AliasDto.

        Has the alias been verified. You must verify an alias if the masked email address has not yet been verified by your account  # noqa: E501

        :param is_verified: The is_verified of this AliasDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_verified is None:  # noqa: E501
            raise ValueError("Invalid value for `is_verified`, must not be `None`")  # noqa: E501

        self._is_verified = is_verified

    @property
    def created_at(self):
        """Gets the created_at of this AliasDto.  # noqa: E501


        :return: The created_at of this AliasDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AliasDto.


        :param created_at: The created_at of this AliasDto.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AliasDto.  # noqa: E501


        :return: The updated_at of this AliasDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AliasDto.


        :param updated_at: The updated_at of this AliasDto.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AliasDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AliasDto):
            return True

        return self.to_dict() != other.to_dict()
