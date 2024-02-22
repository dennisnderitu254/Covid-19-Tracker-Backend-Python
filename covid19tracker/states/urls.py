from django.urls import path
from .views import StateListView

app_name = 'states'

urlpatterns = [
    path('', StateListView.as_view(), name='state-list'),
]
