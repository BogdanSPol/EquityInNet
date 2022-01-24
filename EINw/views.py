from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from validate_email import validate_email


def index(request):
#    return render(request, 'index.html')
    return redirect('equities:equities_index')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def userportfolio(request):
    if request.method == 'GET':
        return render(request, 'usermenu/userportfolio.html')
    else:
        pass


def userfavorite(request):
    if request.method == 'GET':
        return render(request, 'usermenu/userfavorite.html')
    else:
        pass


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'auth/signupuser.html', {'signup_form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            is_valid = validate_email(request.POST['email'], verify=True)
            if is_valid:
                try:
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'auth/signupuser.html',
                                  {'signup_form': UserCreationForm(),
                                   'error': 'That username has already been taken. Please choose a new username'})
            else:
                return render(request, 'auth/signupuser.html',
                              {'signup_form': UserCreationForm(),
                               'error': 'Invalid email'})
        else:
            return render(request, 'auth/signupuser.html',
                          {'signup_form': UserCreationForm(),
                           'error': 'Password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'auth/loginuser.html', {'login_form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/loginuser.html',
                          {'login_form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('index')
