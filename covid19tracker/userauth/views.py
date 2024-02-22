from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def home(request):
    return render(request, 'userauth/home.html')

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
            return render(request, 'userauth/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'userauth/signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'userauth/home.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard:dashboard'))
            # return redirect('/profile') #Profile
        else:
            msg = 'Invalid login credentials'
            form = AuthenticationForm()
            return render(request, 'userauth/signin.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'userauth/signin.html', {'form': form})

def profile(request):
    return render(request, 'userauth/profile.html')

def signout(request):
    logout(request)
    return redirect('/')
