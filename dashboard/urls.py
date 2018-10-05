from django.conf.urls import url, include
from dashboard.views import DashboardView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
]
