import os
from unittest import TestCase

import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ct_board.settings")
django.setup()


class TestSetUpTest(TestCase):
    def setUp(self):
        call_command('migrate', 'board', '0001_initial')
        super().setUp()
