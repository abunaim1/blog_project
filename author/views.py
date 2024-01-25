from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST': 
        register_form = forms.RegistrationForm(request.POST) 
        if register_form.is_valid(): 
            register_form.save() 
            messages.success(request, 'Account created successfully')
            return redirect('register') 
    else: 
        register_form = forms.RegistrationForm() 
    return render(request, 'register.html',{'form':register_form,'type':'Registration'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request, user)
                return redirect('user_login')
            else:
                messages.warning(request, 'Login information incorrect ') 
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form':form, 'type':'Login'})
