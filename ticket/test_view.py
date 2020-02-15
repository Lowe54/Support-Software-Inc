from django.test import Client, TestCase
from django.contrib.auth.models import User
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
        page = self.client.get("/dashboard")
        self.assertEqual(page.status_code, 302)
