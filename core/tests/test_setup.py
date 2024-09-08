from django.test import TestCase

class BasicSetupTests(TestCase):
    def test_project_is_running(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
