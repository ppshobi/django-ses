from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.test import TestCase

import django_ses


class SesImportTest(TestCase):

    def test_it_can_read_given_aws_keys(self,):
        self.assertEquals(settings.SES_ACCESS_KEY, 'xxx')
        self.assertEquals(settings.SES_SECRET_KEY, 'xxx')

    def test_it_can_return_an_email_backend(self):
        self.assertTrue(isinstance(django_ses.SesBackend(), BaseEmailBackend))
