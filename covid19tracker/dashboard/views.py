from django.shortcuts import render
from django.views import View

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')

def allcases(request):
    return render(request, 'dashboard/templates/allcases.html')

def dailyreports(request):
    return render(request, 'dashboard/templates/dailyreports.html')

def confirmedcases(request):
    return render(request, 'dashboard/templates/confirmedcases.html')

def regions(request):
    return render(request, 'dashboard/templates/regions.html')
