from __future__ import unicode_literals

from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
