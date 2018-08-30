from django.conf import settings
from django.test import TestCase
from moto import mock_ses

class SesImportTest(TestCase):

    @mock_ses
    def test_it_can_read_given_aws_keys(self,):
        self.assertEquals(settings.AWS_ACCESS_KEY, 'xxx')
        self.assertEquals(settings.AWS_SECRET_KEY, 'xxx')