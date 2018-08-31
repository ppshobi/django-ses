import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.core import mail
from django.core.mail import EmailMessage
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
        conn = boto3.client('ses', region_name='us-east-1')
        conn.verify_email_identity(EmailAddress="from1@example.com")

        email1 = self.create_email()

        self.assertIsNotNone(email1.send())

    @mock_ses
    def test_it_raises_exception_for_unverified_emails(self):
        email1 = self.create_email()
        self.assertRaises(ClientError, lambda: email1.send())

    @mock_ses
    def test_it_doesnt_raises_exception_if_fail_silently_is_true(self):
        email1 = self.create_email()
        try:
            email1.send(fail_silently=True)
        except ClientError as e:
            self.fail("it raised error even when fail silently is used")

    def test_it_can_return_an_email_backend(self):
        self.assertTrue(isinstance(django_ses.SesBackend(), BaseEmailBackend))

    def create_email(self):
        return EmailMessage(
            'Subject 1',
            'Body1 goes here',
            'from1@example.com',
            ['to1@example.com', 'to2@example.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )


