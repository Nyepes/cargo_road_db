from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(user)
            return redirect('home')
        else:
            messages.success(request, "There was an error")
            return redirect('login_user')
    else:
        return render(request, 'login.html', {})
    