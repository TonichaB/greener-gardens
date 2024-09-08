from django.test import TestCase
from django.apps import apps

class InstalledAppsTests(TestCase):
    def test_core_app_installed(self):
        self.assertTrue(app.is_installed('core'))

