from django.test import TestCase
import environ

class EnvVarsTests(TestCase):
    def setUp(self):
        self.env = environ.Env()
        self.env.read_env()

    def test_secret_key(self):
        self.assertIsNotNone(self.env('SECRET_KEY'))

    def test_debug_setting(self):
        self.assertIsInstance(self.env.bool('DEBUG', default=False), bool)

