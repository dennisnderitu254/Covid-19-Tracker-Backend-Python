from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('allcases/', views.allcases, name='allcases'),
    path('regions/', views.regions, name='regions'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('allcases/', views.allcases, name='allcases'),
    path('dailyreports/', views.dailyreports, name='dailyreports'),
    path('confirmedcases/', views.confirmedcases, name='confirmedcases'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('traveladvice/', views.traveladvice, name='traveladvice'),
    path('search_cases/', views.search_cases, name='search_cases'),
    path('signout/', LogoutView.as_view(), name='signout'),
]
