import unittest
from flask_app import app
import urllib.parse

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)