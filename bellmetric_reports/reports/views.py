from __future__ import unicode_literals

from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import ModelFormMixin

from .models import (
    Company, Campaign, SourceType, Source, Cdr, CdrSource)
from .forms import CampaignForm


class CallsListView(ListView):
    """
        Task 2 a) A list of calls (records in the cdr table) with
        id, call start, campaign name, caller number, called number
        and call duration.
    """

    model = Cdr

    def calls_order_by(self, **kwargs):
        """
            Task 3: Add option(s) for filtering and sorting the call list in
            2(a) by call start date, call start time of day, campaign name,
            caller number, called number and call duration.
        """

        filter_list = [
            'call_start', 'campaign__name', 'caller', 'called', 'call_duration']

        if kwargs.get('o') in filter_list:
            self.queryset = self.model.objects.order_by(kwargs['o'])

    def get(self, request, *args, **kwargs):

        if request.GET.get('o'):
            self.calls_order_by(o=request.GET['o'])

        return super(CallsListView, self).get(request, *args, **kwargs)


class SourceListView(ListView):
    """
        Task 2 b) For a specific call, a list of source records
        ordered by time. Add a link or button to each item in
        the list of calls in 2(a) to display the source records
        for that call.
    """

    model = CdrSource

    def get_queryset(self):
        """Source records filter"""
        self.queryset = self.model.objects.filter(
            cdr=self.kwargs.get('cdr'))

        return self.queryset


class ReportsListView(ListView):
    """
        Task 4 Create a reporting page, where data from the CDR model
        can be aggregated by various fields, e.g. show total calls and
        total duration. Add the ability to filter by campaign and
        source type through the source model.
    """

    model = Cdr
    template_name_suffix = '_page'

    def get(self, request, *args, **kwargs):
        
        self.object_list = self.get_queryset()

        # Search
        if request.GET.get('q'):
            self.object_list = self.object_list.filter(
                campaign__name__icontains=request.GET['q'])

        # Campaign filter
        if request.GET.get('c'):
            self.object_list = self.object_list.filter(
                campaign__id=request.GET['c'])

        # Source type filter
        if request.GET.get('t'):
            cdrsourse_set = CdrSource.objects.filter(
                source__source_type__id=request.GET['t'])
            self.object_list = self.object_list.filter(
                id__in=[obj.cdr.id for obj in cdrsourse_set])
        
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class CampaignUpdateView(UpdateView):
    """
        Task 5: Create a form for updating the campaign model's properties.
        Describe how you would change this form to be submitted by AJAX
        instead of HTTP POST.
    """

    model = Campaign
    form_class = CampaignForm
    template_name = 'reports/campaign_update.html'
    success_url = '/report/campaign/10/update/'
