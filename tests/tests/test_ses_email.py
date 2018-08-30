import boto3
from django.conf import settings
from django.core import mail
from django.core.mail import EmailMessage, send_mail
from django.test import TestCase
from moto import mock_ses


class SesEmail(TestCase):

    def setUp(self):
        mail.original_email_backend = settings.EMAIL_BACKEND
        settings.EMAIL_BACKEND = 'django_ses.SesBackend'

    def test_email_backend_configured(self):
        self.assertEquals(settings.EMAIL_BACKEND, 'django_ses.SesBackend')

    @mock_ses
    def test_it_can_send_email(self):
        conn = boto3.client('ses', region_name='us-east-1')
        conn.verify_email_identity(EmailAddress="from1@shobi.in")

        email1 = EmailMessage(
            'Subject 1',
            'Body1 goes here',
            'from1@shobi.in',
            ['ppshobi@gmail.com'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )

        self.assertIsNotNone(email1.send())
