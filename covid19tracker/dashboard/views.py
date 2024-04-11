from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
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
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Send email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.EMAIL_HOST_USER,
            ['planetnderitu@gmail.com'],  # Send to planetnderitu@gmail.com
            fail_silently=False,
        )

        return render(request, 'dashboard/contact_success.html')

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

