from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password=password
            )
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard:dashboard')) # redirects to the user dashboard with data
            # return redirect('/profile') #Profile
    else:
        msg = 'Error Login'
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'msg' : msg})

def profile(request):
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('/')
