from __future__ import unicode_literals

from random import randrange

from django.contrib.auth.models import User
from django.test import TestCase

from reports.models import CdrSource, Campaign

class ReportPageTest(TestCase):
    """Reporting page test"""

    fixtures = ['reports']

    def test_campaign_empty_search(self):
        """Campaign empty search is working at '/report/?q=' ?"""

        answer = self.client.get('/report/?q=')
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format(
                '/report/?q=', answer.status_code))

    def test_campaign_search(self):
        """Campaign search is working at '/report/?q=<key_word>' ?"""
        
        campaign_set = Campaign.objects.all()

        answer = self.client.get(
            '/report/?q=%s' % campaign_set[
                randrange(campaign_set.count())].name)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format(
                '/report/?q=<key_word>', answer.status_code))

    def test_campaign_filter(self):
        """Campaign filter is working at '/report/?c=<pk>' ?"""

        campaign_set = Campaign.objects.all()

        answer = self.client.get(
            '/report/?c=%s' % campaign_set[
                randrange(campaign_set.count())].id)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format(
                '/report/?c=<pk>', answer.status_code))

    def test_source_type_filter(self):
        """Source type filter is working at '/report/?t=<source_type.id>' ?"""

        cdrsource_set = CdrSource.objects.all()

        answer = self.client.get(
            '/report/?t=%s' % cdrsource_set[
                randrange(cdrsource_set.count())].id)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format(
                '/report/?t=<source_type.id>', answer.status_code))
