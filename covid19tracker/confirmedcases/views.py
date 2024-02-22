# confirmedcases/views.py
from django.views.generic import ListView
from .models import ConfirmedCase

class ConfirmedCaseListView(ListView):
    model = ConfirmedCase
    template_name = 'confirmedcases/case_list.html'
    context_object_name = 'cases'





