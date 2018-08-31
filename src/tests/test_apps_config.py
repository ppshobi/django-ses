from django.test import TestCase

from django_ses.apps import DjangoSesConfig


class DjangoSesConfigTest(TestCase):
    def test_apps(self):
        self.assertEquals(DjangoSesConfig.name, 'django_ses')
