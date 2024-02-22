from django.urls import path
from .views import ConfirmedCaseListView

app_name = 'confirmedcases'

urlpatterns = [
    path('list/', ConfirmedCaseListView.as_view(), name='case-list'),
]
