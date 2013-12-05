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
