import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ct_board.settings")
django.setup()

from django.test import TestCase
from django.urls import reverse
from field.models import Fields


class FieldAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.field_model = Fields.objects.create(
            name='Test Field'
        )

    def test_get_field(self):
        url = reverse('getFieldInfo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
