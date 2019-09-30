from django.test import TestCase


# Create your tests here.
class GenericAppTestCase(TestCase):
    """Generic tests"""

    def test_heroku_ci(self):
        """Empty test for Heroku CI initialization"""
        return True
