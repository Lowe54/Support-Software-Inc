'''
Test page for the Ticket Model
'''
from datetime import datetime

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from authentication.models import MyUser

from .models import Ticket


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
            raised_by=MyUser.objects.get(user_id=self.user.id),
            raised_on=datetime.now(),
        )
        test_ticket.save()

        self.assertEqual(test_ticket.status, 'OPN')

    def test_initial_priority(self):
        '''
        Does the initial priority default to 'LOW'
        '''
        test_ticket = Ticket(
            title='Test',
            description='Test',
            raised_by=MyUser.objects.get(user_id=self.user.id),
            raised_on=datetime.now(),
        )
        test_ticket.save()

        self.assertEqual(test_ticket.priority, 'LOW')
