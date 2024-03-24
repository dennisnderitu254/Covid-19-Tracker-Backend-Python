from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from .models import Cases

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')

def allcases(request):
    all_cases = Cases.objects.all()
    return render(request, 'dashboard/allcases.html', {'all_cases': all_cases})

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

def search_cases(request):
    search_query = request.GET.get('search_query', '')
    
    # Perform a case-insensitive search in the state field
    cases = Cases.objects.filter(state__icontains=search_query)
    
    return render(request, 'dashboard/search_cases.html', {'cases': cases, 'search_query': search_query})

def signout(request):
    logout(request)
    return redirect('/')

