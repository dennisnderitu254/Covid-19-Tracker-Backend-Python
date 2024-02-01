from django.urls import path
from .views import signup, signin, profile, signout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('profile/', profile, name='profile'),
    path('signout/', signout, name='signout'),
]
