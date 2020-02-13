'''
Test suite for Ticket Module
'''
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from authentication.models import MyUser
from .models import Ticket
# Create your tests here.

class TestTicketModel(TestCase):
    '''
    Suite of tests for the Ticket model
    '''
    def setUp(self):
        '''
        Setup MyUser instance
        '''
        self.factory = RequestFactory()
        user = User.objects.create_user(
            username='jacob',
            email='jacob@…',
            password='top_secret'
        )
        user.save()
        self.user = MyUser.objects.create(
            user=User.objects.get(pk=user.id),
            role='AGN'
        )

    def test_initial_status(self):
        '''
        Does the initial status default to 'OPN'
        '''
        test_ticket = Ticket(
            title='Test',
            description='Test',
            raised_by=MyUser.objects.get(user_id=self.user.id)
        )
        test_ticket.save()

        self.assertEqual(test_ticket.status, 'OPN')

    def test_initial_priority(self):
        '''
        Does the initial priority default to 'OPN'
        '''
        test_ticket = Ticket(
            title='Test',
            description='Test',
            raised_by=MyUser.objects.get(user_id=self.user.id)
        )
        test_ticket.save()

        self.assertEqual(test_ticket.priority, 'LOW')
        