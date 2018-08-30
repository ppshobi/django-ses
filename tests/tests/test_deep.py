from __future__ import absolute_import, unicode_literals


from django.test import TestCase
from django.urls import reverse


class DeepThoughtTestCase(TestCase):

    def test_deepthought_view(self):
        response = self.client.get(reverse("django_deepthought"))
        self.assertEqual(response.content, b"42")