from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'index.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'auth/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('equities:equities_index')
            except IntegrityError:
                return render(request, 'auth/signupuser.html',
                              {'form': UserCreationForm(), 'error':
                                  'That username has already been taken. Please choose a new username'})

        else:
            return render(request, 'auth/signupuser.html',
                          {'form': UserCreationForm(), 'error':
                              'Password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'auth/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('index')


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
