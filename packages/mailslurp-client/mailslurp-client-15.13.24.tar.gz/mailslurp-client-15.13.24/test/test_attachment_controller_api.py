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

import mailslurp_client
from mailslurp_client.api.attachment_controller_api import AttachmentControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestAttachmentControllerApi(unittest.TestCase):
    """AttachmentControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.attachment_controller_api.AttachmentControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_all_attachments(self):
        """Test case for delete_all_attachments

        Delete all attachments  # noqa: E501
        """
        pass

    def test_delete_attachment(self):
        """Test case for delete_attachment

        Delete an attachment  # noqa: E501
        """
        pass

    def test_download_attachment_as_base64_encoded(self):
        """Test case for download_attachment_as_base64_encoded

        Get email attachment as base64 encoded string as alternative to binary responses. To read the content decode the Base64 encoded contents.  # noqa: E501
        """
        pass

    def test_download_attachment_as_bytes(self):
        """Test case for download_attachment_as_bytes

        Download attachments. Get email attachment bytes. If you have trouble with byte responses try the `downloadAttachmentBase64` response endpoints.  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Get an attachment entity  # noqa: E501
        """
        pass

    def test_get_attachment_info(self):
        """Test case for get_attachment_info

        Get email attachment metadata information  # noqa: E501
        """
        pass

    def test_get_attachments(self):
        """Test case for get_attachments

        Get email attachments  # noqa: E501
        """
        pass

    def test_upload_attachment(self):
        """Test case for upload_attachment

        Upload an attachment for sending using base64 file encoding. Returns an array whose first element is the ID of the uploaded attachment.  # noqa: E501
        """
        pass

    def test_upload_attachment_bytes(self):
        """Test case for upload_attachment_bytes

        Upload an attachment for sending using file byte stream input octet stream. Returns an array whose first element is the ID of the uploaded attachment.  # noqa: E501
        """
        pass

    def test_upload_multipart_form(self):
        """Test case for upload_multipart_form

        Upload an attachment for sending using a Multipart Form request. Returns an array whose first element is the ID of the uploaded attachment.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
