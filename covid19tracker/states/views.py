from django.shortcuts import render
from django.views.generic import ListView
from .models import State

class StateListView(ListView):
    model = State
    template_name = 'states/state_list.html'  
    context_object_name = 'states'

