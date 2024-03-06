from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')

def allcases(request):
    return render(request, 'dashboard/allcases.html')

def dailyreports(request):
    return render(request, 'dashboard/dailyreports.html')

def confirmedcases(request):
    return render(request, 'dashboard/confirmedcases.html')

def regions(request):
    return render(request, 'dashboard/regions.html')

def about(request):
    return render(request, 'dashboard/about.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def traveladvice(request):
    return render(request, 'dashboard/traveladvice.html')

def signout(request):
    logout(request)
    return redirect('/')

