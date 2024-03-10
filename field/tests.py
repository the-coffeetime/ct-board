import os

import django
from rest_framework import status

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ct_board.settings")
django.setup()

from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from field.models import Fields


class FieldAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.field_model = Fields.objects.create(
            name='Test Field',
        )

    def test_get_field(self):
        url = reverse('getFieldInfo')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
