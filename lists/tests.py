from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_math(self):
        self.asssertEqual(1+1,3)
# Create your tests here.
