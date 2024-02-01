# views.py

from django.shortcuts import render
from .models import Covid19Data

def dashboard(request):
    user_country = "User's Country"  # Replace with logic to get the user's country

    data = Covid19Data.objects.filter(countryid__name=user_country).order_by('-date')[:10]

    context = {
        'user_country': user_country,
        'data': data,
    }

    return render(request, 'dashboard/dashboard.html', context)
