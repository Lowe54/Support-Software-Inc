'''
Test file for Ticket views
'''
from django.contrib.auth.models import User
from django.test import Client, TestCase

from authentication.models import MyUser


class TestTicketViews(TestCase):
    '''
    Suite of tests for the Ticket model
    '''
    def setUp(self):
        '''
        Setup MyUser instance
        '''

        validuser = User.objects.create_user(
            username='jacob',
            email='jacob@…',
            password='top_secret'
        )
        validuser.save()
        self.validuser = MyUser.objects.create(
            user=User.objects.get(pk=validuser.id),
            role='USR'
        )

        self.client = Client()

    #####################
    # DASHBOARD
    #####################

    def test_get_dashboard_not_logged_in(self):
        '''
        Ensure that the return code for the dashboard
        is 302 if the user is not signed in
        '''
        page = self.client.get("/dashboard")
        self.assertEqual(page.status_code, 302)

    def test_get_dashboard_logged_in(self):
        '''
        Ensure that the return code for the dashboard
        is 200 if the user is signed in
        '''
        self.client.login(username='jacob', password='top_secret')
        page = self.client.get("/dashboard")
        self.assertEqual(page.status_code, 200)
