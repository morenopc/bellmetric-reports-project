from __future__ import unicode_literals

from random import randrange

from django.contrib.auth.models import User
from django.test import TestCase

from reports.models import Cdr, Campaign

class PagesTest(TestCase):
    """Get project pages test"""

    fixtures = ['reports']

    def setUp(self):
        user = User.objects.create_user(
            'nosetest', 'nose@test.com', 'nosetest')
        self.client.login(username='nosetest', password='nosetest')

    def test_home(self):
        """Home page is working at '/' ?"""
        answer = self.client.get('/', follow=True)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format('/', answer.status_code))

    def test_report_page(self):
        """Report page is working at '/report/' ?"""
        answer = self.client.get('/report/', follow=True)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format('/report/', answer.status_code))

    def test_calls(self):
        """Calls page is working at '/report/calls/' ?"""
        answer = self.client.get('/report/calls/', follow=True)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format('/report/calls/', answer.status_code))

    def test_call_source(self):
        """Call source page is working ?"""
        answer = self.client.get(
            '/report/call/%s/source/' % randrange(
                Cdr.objects.all().count()))
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format(
                '/report/call/(?P<cdr>\d+)/source/',
                answer.status_code))

    def test_campaign_update(self):
        """Campaign update page is working ?"""
        answer = self.client.get(
            '/report/campaign/%s/update/' % randrange(
                Campaign.objects.all().count()))
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format(
                '/report/campaign/(?P<pk>\d+)/update/',
                answer.status_code))