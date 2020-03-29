'''
Tests file for Authentication module
'''
from django.test import TestCase


class TestAuthenticationViews(TestCase):
    '''
    Suite of tests for the Core module
    '''
    def test_login_page_loads(self):
        '''
        Ensure that the return code for the login page
        is 200
        '''
        page = self.client.get("/auth/login")
        self.assertEqual(page.status_code, 200)

    def test_register_page_loads(self):
        '''
        Ensure that the return code for the register page
        is 200
        '''
        page = self.client.get("/auth/register")
        self.assertEqual(page.status_code, 200)
