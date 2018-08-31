from django.conf import settings
from django.test import TestCase


class SesImportTest(TestCase):

    def test_it_can_read_given_aws_keys(self,):
        self.assertEquals(settings.AWS_ACCESS_KEY, 'xxx')
        self.assertEquals(settings.AWS_SECRET_KEY, 'xxx')