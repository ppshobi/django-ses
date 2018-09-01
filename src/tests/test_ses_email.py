import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.core import mail
from django.core.mail import EmailMessage, send_mail, send_mass_mail
from django.core.mail.backends.base import BaseEmailBackend
from django.test import TestCase
from moto import mock_ses

import django_ses


class SesEmail(TestCase):

    def setUp(self):
        mail.original_email_backend = settings.EMAIL_BACKEND
        settings.EMAIL_BACKEND = 'django_ses.SesBackend'

    def test_email_backend_configured(self):
        self.assertEquals(settings.EMAIL_BACKEND, 'django_ses.SesBackend')

    @mock_ses
    def test_it_can_send_email_from_verified_email(self):
        self.setup_boto3_client()
        email = self.create_email()

        self.assertIsNotNone(email.send())

    @mock_ses
    def test_it_raises_exception_for_unverified_emails(self):
        email = self.create_email()

        self.assertRaises(ClientError, lambda: email.send())

    def test_it_doesnt_raise_exception_if_fail_silently_is_true(self):
        email = self.create_email()
        try:
            email.send(fail_silently=True)
        except ClientError as e:
            self.fail("it raised error even when fail silently is used")
        else:
            self.assertTrue(True, msg="test passed because it failed silently")

    @mock_ses
    def test_send_email_function(self):
        self.setup_boto3_client()
        self.assertIsNotNone(send_mail(subject="Test Subject", message="Message", from_email="from@example.com", recipient_list=['to@example.com']))

    @mock_ses
    def test_send_mass_email_function(self):
        self.setup_boto3_client()

        message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
        message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])

        self.assertIsNotNone(send_mass_mail((message1, message2), fail_silently=False))

    def test_it_can_return_an_email_backend(self):
        self.assertTrue(isinstance(django_ses.SesBackend(), BaseEmailBackend))

    def setup_boto3_client(self):
        client = boto3.client('ses', region_name='us-east-1', aws_access_key_id=settings.AWS_ACCESS_KEY,
                              aws_secret_access_key=settings.AWS_SECRET_KEY)
        client.verify_email_identity(EmailAddress="from@example.com")

    def create_email(self):
        return EmailMessage(
            'Subject 1',
            'Body1 goes here',
            'from@example.com',
            ['to1@example.com', 'to2@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )


