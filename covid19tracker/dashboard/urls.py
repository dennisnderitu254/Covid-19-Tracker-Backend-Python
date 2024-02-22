from django.urls import path
from .views import DashboardView, allcases, dailyreports, confirmedcases, regions

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('allcases/', allcases, name='allcases'),
    path('dailyreports/', dailyreports, name='dailyreports'),
    path('confirmedcases/', confirmedcases, name='confirmedcases'),
    path('regions/', regions, name='regions'),
]
