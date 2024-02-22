from django.contrib import admin
from django.urls import include, path
from userauth import views
from confirmedcases.urls import urlpatterns as confirmedcases_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userauth.urls')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('userauth/', include('userauth.urls')),
    path('confirmedcases/', include('confirmedcases.urls')),
    path('states/', include('states.urls')),
    path('reports/', include('reports.urls')),
]
