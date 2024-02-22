from django.urls import path
from userauth import views

# urlpatterns = [
#     path('signup/', signup, name='signup'),
#     path('signin/', signin, name='signin'),
#     path('profile/', profile, name='profile'),
#     path('signout/', signout, name='signout'),
# ]

urlpatterns = [
    path('', views.home),
    path('signin/', views.signin, name='signin'),
    path('signup', views.signup),
    path('signout', views.signout),
    path('profile', views.profile),
]
