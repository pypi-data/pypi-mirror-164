# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.wait_for_single_sms_options import WaitForSingleSmsOptions  # noqa: E501
from mailslurp_client.rest import ApiException

class TestWaitForSingleSmsOptions(unittest.TestCase):
    """WaitForSingleSmsOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WaitForSingleSmsOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.wait_for_single_sms_options.WaitForSingleSmsOptions()  # noqa: E501
        if include_optional :
            return WaitForSingleSmsOptions(
                phone_number_id = '0', 
                timeout = 56, 
                unread_only = True, 
                before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                sort_direction = 'ASC', 
                delay = 56
            )
        else :
            return WaitForSingleSmsOptions(
                phone_number_id = '0',
                timeout = 56,
        )

    def testWaitForSingleSmsOptions(self):
        """Test WaitForSingleSmsOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
