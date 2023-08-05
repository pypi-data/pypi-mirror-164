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


class WaitForSmsConditions(object):
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
        'phone_number_id': 'str',
        'limit': 'int',
        'count': 'int',
        'delay_timeout': 'int',
        'timeout': 'int',
        'unread_only': 'bool',
        'count_type': 'str',
        'matches': 'list[SmsMatchOption]',
        'sort_direction': 'str',
        'since': 'datetime',
        'before': 'datetime'
    }

    attribute_map = {
        'phone_number_id': 'phoneNumberId',
        'limit': 'limit',
        'count': 'count',
        'delay_timeout': 'delayTimeout',
        'timeout': 'timeout',
        'unread_only': 'unreadOnly',
        'count_type': 'countType',
        'matches': 'matches',
        'sort_direction': 'sortDirection',
        'since': 'since',
        'before': 'before'
    }

    def __init__(self, phone_number_id=None, limit=None, count=None, delay_timeout=None, timeout=None, unread_only=None, count_type=None, matches=None, sort_direction=None, since=None, before=None, local_vars_configuration=None):  # noqa: E501
        """WaitForSmsConditions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._phone_number_id = None
        self._limit = None
        self._count = None
        self._delay_timeout = None
        self._timeout = None
        self._unread_only = None
        self._count_type = None
        self._matches = None
        self._sort_direction = None
        self._since = None
        self._before = None
        self.discriminator = None

        self.phone_number_id = phone_number_id
        if limit is not None:
            self.limit = limit
        self.count = count
        if delay_timeout is not None:
            self.delay_timeout = delay_timeout
        self.timeout = timeout
        if unread_only is not None:
            self.unread_only = unread_only
        if count_type is not None:
            self.count_type = count_type
        if matches is not None:
            self.matches = matches
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if since is not None:
            self.since = since
        if before is not None:
            self.before = before

    @property
    def phone_number_id(self):
        """Gets the phone_number_id of this WaitForSmsConditions.  # noqa: E501

        ID of phone number to search within and apply conditions to. Essentially filtering the SMS found to give a count.  # noqa: E501

        :return: The phone_number_id of this WaitForSmsConditions.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_id

    @phone_number_id.setter
    def phone_number_id(self, phone_number_id):
        """Sets the phone_number_id of this WaitForSmsConditions.

        ID of phone number to search within and apply conditions to. Essentially filtering the SMS found to give a count.  # noqa: E501

        :param phone_number_id: The phone_number_id of this WaitForSmsConditions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone_number_id is None:  # noqa: E501
            raise ValueError("Invalid value for `phone_number_id`, must not be `None`")  # noqa: E501

        self._phone_number_id = phone_number_id

    @property
    def limit(self):
        """Gets the limit of this WaitForSmsConditions.  # noqa: E501

        Limit results  # noqa: E501

        :return: The limit of this WaitForSmsConditions.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this WaitForSmsConditions.

        Limit results  # noqa: E501

        :param limit: The limit of this WaitForSmsConditions.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def count(self):
        """Gets the count of this WaitForSmsConditions.  # noqa: E501

        Number of results that should match conditions. Either exactly or at least this amount based on the `countType`. If count condition is not met and the timeout has not been reached the `waitFor` method will retry the operation.  # noqa: E501

        :return: The count of this WaitForSmsConditions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this WaitForSmsConditions.

        Number of results that should match conditions. Either exactly or at least this amount based on the `countType`. If count condition is not met and the timeout has not been reached the `waitFor` method will retry the operation.  # noqa: E501

        :param count: The count of this WaitForSmsConditions.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def delay_timeout(self):
        """Gets the delay_timeout of this WaitForSmsConditions.  # noqa: E501

        Max time in milliseconds to wait between retries if a `timeout` is specified.  # noqa: E501

        :return: The delay_timeout of this WaitForSmsConditions.  # noqa: E501
        :rtype: int
        """
        return self._delay_timeout

    @delay_timeout.setter
    def delay_timeout(self, delay_timeout):
        """Sets the delay_timeout of this WaitForSmsConditions.

        Max time in milliseconds to wait between retries if a `timeout` is specified.  # noqa: E501

        :param delay_timeout: The delay_timeout of this WaitForSmsConditions.  # noqa: E501
        :type: int
        """

        self._delay_timeout = delay_timeout

    @property
    def timeout(self):
        """Gets the timeout of this WaitForSmsConditions.  # noqa: E501

        Max time in milliseconds to retry the `waitFor` operation until conditions are met.  # noqa: E501

        :return: The timeout of this WaitForSmsConditions.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this WaitForSmsConditions.

        Max time in milliseconds to retry the `waitFor` operation until conditions are met.  # noqa: E501

        :param timeout: The timeout of this WaitForSmsConditions.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501

        self._timeout = timeout

    @property
    def unread_only(self):
        """Gets the unread_only of this WaitForSmsConditions.  # noqa: E501

        Apply conditions only to **unread** SMS. All SMS messages begin with `read=false`. An SMS is marked `read=true` when an `SMS` has been returned to the user at least once. For example you have called `getSms` or `waitForSms` etc., or you have viewed the SMS in the dashboard.  # noqa: E501

        :return: The unread_only of this WaitForSmsConditions.  # noqa: E501
        :rtype: bool
        """
        return self._unread_only

    @unread_only.setter
    def unread_only(self, unread_only):
        """Sets the unread_only of this WaitForSmsConditions.

        Apply conditions only to **unread** SMS. All SMS messages begin with `read=false`. An SMS is marked `read=true` when an `SMS` has been returned to the user at least once. For example you have called `getSms` or `waitForSms` etc., or you have viewed the SMS in the dashboard.  # noqa: E501

        :param unread_only: The unread_only of this WaitForSmsConditions.  # noqa: E501
        :type: bool
        """

        self._unread_only = unread_only

    @property
    def count_type(self):
        """Gets the count_type of this WaitForSmsConditions.  # noqa: E501

        How result size should be compared with the expected size. Exactly or at-least matching result?  # noqa: E501

        :return: The count_type of this WaitForSmsConditions.  # noqa: E501
        :rtype: str
        """
        return self._count_type

    @count_type.setter
    def count_type(self, count_type):
        """Sets the count_type of this WaitForSmsConditions.

        How result size should be compared with the expected size. Exactly or at-least matching result?  # noqa: E501

        :param count_type: The count_type of this WaitForSmsConditions.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXACTLY", "ATLEAST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and count_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `count_type` ({0}), must be one of {1}"  # noqa: E501
                .format(count_type, allowed_values)
            )

        self._count_type = count_type

    @property
    def matches(self):
        """Gets the matches of this WaitForSmsConditions.  # noqa: E501

        Conditions that should be matched for an SMS to qualify for results. Each condition will be applied in order to each SMS within a phone number to filter a result list of matching SMSs you are waiting for.  # noqa: E501

        :return: The matches of this WaitForSmsConditions.  # noqa: E501
        :rtype: list[SmsMatchOption]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this WaitForSmsConditions.

        Conditions that should be matched for an SMS to qualify for results. Each condition will be applied in order to each SMS within a phone number to filter a result list of matching SMSs you are waiting for.  # noqa: E501

        :param matches: The matches of this WaitForSmsConditions.  # noqa: E501
        :type: list[SmsMatchOption]
        """

        self._matches = matches

    @property
    def sort_direction(self):
        """Gets the sort_direction of this WaitForSmsConditions.  # noqa: E501

        Direction to sort matching SMSs by created time  # noqa: E501

        :return: The sort_direction of this WaitForSmsConditions.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this WaitForSmsConditions.

        Direction to sort matching SMSs by created time  # noqa: E501

        :param sort_direction: The sort_direction of this WaitForSmsConditions.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sort_direction not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sort_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_direction, allowed_values)
            )

        self._sort_direction = sort_direction

    @property
    def since(self):
        """Gets the since of this WaitForSmsConditions.  # noqa: E501

        ISO Date Time earliest time of SMS to consider. Filter for matching SMSs that were received after this date  # noqa: E501

        :return: The since of this WaitForSmsConditions.  # noqa: E501
        :rtype: datetime
        """
        return self._since

    @since.setter
    def since(self, since):
        """Sets the since of this WaitForSmsConditions.

        ISO Date Time earliest time of SMS to consider. Filter for matching SMSs that were received after this date  # noqa: E501

        :param since: The since of this WaitForSmsConditions.  # noqa: E501
        :type: datetime
        """

        self._since = since

    @property
    def before(self):
        """Gets the before of this WaitForSmsConditions.  # noqa: E501

        ISO Date Time latest time of SMS to consider. Filter for matching SMSs that were received before this date  # noqa: E501

        :return: The before of this WaitForSmsConditions.  # noqa: E501
        :rtype: datetime
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this WaitForSmsConditions.

        ISO Date Time latest time of SMS to consider. Filter for matching SMSs that were received before this date  # noqa: E501

        :param before: The before of this WaitForSmsConditions.  # noqa: E501
        :type: datetime
        """

        self._before = before

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
        if not isinstance(other, WaitForSmsConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WaitForSmsConditions):
            return True

        return self.to_dict() != other.to_dict()
