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


class TrackingPixelDto(object):
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
        'seen': 'bool',
        'recipient': 'str',
        'html': 'str',
        'url': 'str',
        'inbox_id': 'str',
        'sent_email_id': 'str',
        'seen_at': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'seen': 'seen',
        'recipient': 'recipient',
        'html': 'html',
        'url': 'url',
        'inbox_id': 'inboxId',
        'sent_email_id': 'sentEmailId',
        'seen_at': 'seenAt',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, seen=None, recipient=None, html=None, url=None, inbox_id=None, sent_email_id=None, seen_at=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """TrackingPixelDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._seen = None
        self._recipient = None
        self._html = None
        self._url = None
        self._inbox_id = None
        self._sent_email_id = None
        self._seen_at = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.seen = seen
        if recipient is not None:
            self.recipient = recipient
        self.html = html
        self.url = url
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if sent_email_id is not None:
            self.sent_email_id = sent_email_id
        if seen_at is not None:
            self.seen_at = seen_at
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this TrackingPixelDto.  # noqa: E501


        :return: The id of this TrackingPixelDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackingPixelDto.


        :param id: The id of this TrackingPixelDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def seen(self):
        """Gets the seen of this TrackingPixelDto.  # noqa: E501


        :return: The seen of this TrackingPixelDto.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this TrackingPixelDto.


        :param seen: The seen of this TrackingPixelDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and seen is None:  # noqa: E501
            raise ValueError("Invalid value for `seen`, must not be `None`")  # noqa: E501

        self._seen = seen

    @property
    def recipient(self):
        """Gets the recipient of this TrackingPixelDto.  # noqa: E501


        :return: The recipient of this TrackingPixelDto.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this TrackingPixelDto.


        :param recipient: The recipient of this TrackingPixelDto.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def html(self):
        """Gets the html of this TrackingPixelDto.  # noqa: E501


        :return: The html of this TrackingPixelDto.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this TrackingPixelDto.


        :param html: The html of this TrackingPixelDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and html is None:  # noqa: E501
            raise ValueError("Invalid value for `html`, must not be `None`")  # noqa: E501

        self._html = html

    @property
    def url(self):
        """Gets the url of this TrackingPixelDto.  # noqa: E501


        :return: The url of this TrackingPixelDto.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TrackingPixelDto.


        :param url: The url of this TrackingPixelDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def inbox_id(self):
        """Gets the inbox_id of this TrackingPixelDto.  # noqa: E501


        :return: The inbox_id of this TrackingPixelDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this TrackingPixelDto.


        :param inbox_id: The inbox_id of this TrackingPixelDto.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def sent_email_id(self):
        """Gets the sent_email_id of this TrackingPixelDto.  # noqa: E501


        :return: The sent_email_id of this TrackingPixelDto.  # noqa: E501
        :rtype: str
        """
        return self._sent_email_id

    @sent_email_id.setter
    def sent_email_id(self, sent_email_id):
        """Sets the sent_email_id of this TrackingPixelDto.


        :param sent_email_id: The sent_email_id of this TrackingPixelDto.  # noqa: E501
        :type: str
        """

        self._sent_email_id = sent_email_id

    @property
    def seen_at(self):
        """Gets the seen_at of this TrackingPixelDto.  # noqa: E501


        :return: The seen_at of this TrackingPixelDto.  # noqa: E501
        :rtype: datetime
        """
        return self._seen_at

    @seen_at.setter
    def seen_at(self, seen_at):
        """Sets the seen_at of this TrackingPixelDto.


        :param seen_at: The seen_at of this TrackingPixelDto.  # noqa: E501
        :type: datetime
        """

        self._seen_at = seen_at

    @property
    def created_at(self):
        """Gets the created_at of this TrackingPixelDto.  # noqa: E501


        :return: The created_at of this TrackingPixelDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrackingPixelDto.


        :param created_at: The created_at of this TrackingPixelDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if not isinstance(other, TrackingPixelDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackingPixelDto):
            return True

        return self.to_dict() != other.to_dict()
