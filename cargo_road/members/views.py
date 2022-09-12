from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from members.forms import RegisterUserForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username + password)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error")
            return redirect('login_user')
    else:
        return render(request, 'login.html', {})

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            pass1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password = pass1)
            login(request, user)
            messages.success(request, "Succesful Registration")
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form})

@login_required
def logout_user(request):
    messages.success(request, 'Logged Out')
    logout(request)
    return redirect('home')
    