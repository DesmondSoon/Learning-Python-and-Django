from django.shortcuts import render, get_object_or_404, redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect

from accounts.forms import RegistrationForm, EditUserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import (

    # password_reset,
    # password_reset_done,

    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    LogoutView,
    LoginView,
)
from .models import accounts

class PasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset_form.html"

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"

class LoginView(LoginView):
    template_name = "accounts/login.html"

def home(request):

    numbers = [1,2,3,4,5]
    name = "Desmond Soon"

    context = {
        'name':name,
        'numbers':numbers
}
    return render (request,'accounts/home.html',context)

class LogoutView(LogoutView):
    template_name = "accounts/logout.html"


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')

    else:
        form = RegistrationForm()

        args = {'form':form}
        return render (request,'accounts/reg_form.html', args)

def profile(request):

    user = {'user': request.user}
    return render (request,'accounts/profile.html', user)

def edit_profile(request):
    if request.method == 'POST':
        form = EditUserProfile(request.POST, instance=request.user )
        if form.is_valid():
            form.save()
            return redirect ('/accounts/profile')
    else:
        form = EditUserProfile(instance=request.user)

        args ={'form':form}

        return render(request,'accounts/edit_profile.html',args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect ('/accounts/profile')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {"form":form}

        return render (request,'accounts/change_password.html',args)
