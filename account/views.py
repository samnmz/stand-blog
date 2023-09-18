from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from account.forms import LoginForm, EditUserForm


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect(reverse('home:home'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_register(request):
    if request.user.is_authenticated == True:
        return redirect(reverse('home:home'))
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = User.objects.create(username=username, password=password, email=email)
        login(request, user)
        return redirect(reverse('home:home'))
    return render(request, 'account/register.html')


def user_edit(request):
    user = request.user
    form = EditUserForm(instance=user)
    if request.method == 'POST':
        form = EditUserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/user_edit.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(reverse('home:home'))
