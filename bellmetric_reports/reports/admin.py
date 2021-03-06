from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Company, Campaign, SourceType, Source, Cdr, CdrSource)


class CompanyAdmin(admin.ModelAdmin):
    """Company admin"""
    pass

admin.site.register(Company, CompanyAdmin)


class CampaignAdmin(admin.ModelAdmin):
    """Campaign admin"""
    pass

admin.site.register(Campaign, CampaignAdmin)


class SourceTypeAdmin(admin.ModelAdmin):
    """SourceType admin"""
    pass

admin.site.register(SourceType, SourceTypeAdmin)


class SourceAdmin(admin.ModelAdmin):
    """Source admin"""
    pass

admin.site.register(Source, SourceAdmin)


class CdrAdmin(admin.ModelAdmin):
    """Cdr admin"""
    list_display = ('id', 'call_start', 'campaign',
        'caller', 'called', 'call_duration')

admin.site.register(Cdr, CdrAdmin)


class CdrSourceAdmin(admin.ModelAdmin):
    """CdrSource admin"""
    pass

admin.site.register(CdrSource, CdrSourceAdmin)
