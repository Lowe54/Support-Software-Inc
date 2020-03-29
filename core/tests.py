'''
Core module tests.py file
'''
from django.test import TestCase


class TestCoreViews(TestCase):
    '''
    Suite of tests for the Core module
    '''
    def test_core_page_loads(self):
        '''
        Ensure that the return code for the index page
        is 200
        '''
        page = self.client.get("/index")
        self.assertEqual(page.status_code, 200)

