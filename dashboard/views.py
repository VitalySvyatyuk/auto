from django.shortcuts import render
from django.views import View


class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):

        context = {'one': 'one'}
        return render(request, self.template_name, {'context': context})
