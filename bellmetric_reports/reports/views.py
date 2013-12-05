from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from .models import (
    Company, Campaign, SourceType, Source, Cdr, CdrSource)


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
