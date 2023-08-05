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


class EmailPreview(object):
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
        'domain_id': 'str',
        'subject': 'str',
        'to': 'list[str]',
        '_from': 'str',
        'bcc': 'list[str]',
        'cc': 'list[str]',
        'created_at': 'datetime',
        'read': 'bool',
        'attachments': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domainId',
        'subject': 'subject',
        'to': 'to',
        '_from': 'from',
        'bcc': 'bcc',
        'cc': 'cc',
        'created_at': 'createdAt',
        'read': 'read',
        'attachments': 'attachments'
    }

    def __init__(self, id=None, domain_id=None, subject=None, to=None, _from=None, bcc=None, cc=None, created_at=None, read=None, attachments=None, local_vars_configuration=None):  # noqa: E501
        """EmailPreview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._domain_id = None
        self._subject = None
        self._to = None
        self.__from = None
        self._bcc = None
        self._cc = None
        self._created_at = None
        self._read = None
        self._attachments = None
        self.discriminator = None

        self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        self.subject = subject
        self.to = to
        self._from = _from
        self.bcc = bcc
        self.cc = cc
        self.created_at = created_at
        self.read = read
        self.attachments = attachments

    @property
    def id(self):
        """Gets the id of this EmailPreview.  # noqa: E501

        ID of the email entity  # noqa: E501

        :return: The id of this EmailPreview.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailPreview.

        ID of the email entity  # noqa: E501

        :param id: The id of this EmailPreview.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this EmailPreview.  # noqa: E501

        ID of the domain that received the email  # noqa: E501

        :return: The domain_id of this EmailPreview.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this EmailPreview.

        ID of the domain that received the email  # noqa: E501

        :param domain_id: The domain_id of this EmailPreview.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def subject(self):
        """Gets the subject of this EmailPreview.  # noqa: E501

        The subject line of the email message as specified by SMTP subject header  # noqa: E501

        :return: The subject of this EmailPreview.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailPreview.

        The subject line of the email message as specified by SMTP subject header  # noqa: E501

        :param subject: The subject of this EmailPreview.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def to(self):
        """Gets the to of this EmailPreview.  # noqa: E501

        List of `To` recipient email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The to of this EmailPreview.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EmailPreview.

        List of `To` recipient email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param to: The to of this EmailPreview.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this EmailPreview.  # noqa: E501

        Who the email was sent from. An email address - see fromName for the sender name.  # noqa: E501

        :return: The _from of this EmailPreview.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EmailPreview.

        Who the email was sent from. An email address - see fromName for the sender name.  # noqa: E501

        :param _from: The _from of this EmailPreview.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def bcc(self):
        """Gets the bcc of this EmailPreview.  # noqa: E501

        List of `BCC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The bcc of this EmailPreview.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this EmailPreview.

        List of `BCC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param bcc: The bcc of this EmailPreview.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def cc(self):
        """Gets the cc of this EmailPreview.  # noqa: E501

        List of `CC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The cc of this EmailPreview.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this EmailPreview.

        List of `CC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param cc: The cc of this EmailPreview.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def created_at(self):
        """Gets the created_at of this EmailPreview.  # noqa: E501

        When was the email received by MailSlurp  # noqa: E501

        :return: The created_at of this EmailPreview.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EmailPreview.

        When was the email received by MailSlurp  # noqa: E501

        :param created_at: The created_at of this EmailPreview.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def read(self):
        """Gets the read of this EmailPreview.  # noqa: E501

        Read flag. Has the email ever been viewed in the dashboard or fetched via the API with a hydrated body? If so the email is marked as read. Paginated results do not affect read status. Read status is different to email opened event as it depends on your own account accessing the email. Email opened is determined by tracking pixels sent to other uses if enable during sending. You can listened for both email read and email opened events using webhooks.  # noqa: E501

        :return: The read of this EmailPreview.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this EmailPreview.

        Read flag. Has the email ever been viewed in the dashboard or fetched via the API with a hydrated body? If so the email is marked as read. Paginated results do not affect read status. Read status is different to email opened event as it depends on your own account accessing the email. Email opened is determined by tracking pixels sent to other uses if enable during sending. You can listened for both email read and email opened events using webhooks.  # noqa: E501

        :param read: The read of this EmailPreview.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

    @property
    def attachments(self):
        """Gets the attachments of this EmailPreview.  # noqa: E501

        List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension.  # noqa: E501

        :return: The attachments of this EmailPreview.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this EmailPreview.

        List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension.  # noqa: E501

        :param attachments: The attachments of this EmailPreview.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

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
        if not isinstance(other, EmailPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailPreview):
            return True

        return self.to_dict() != other.to_dict()
