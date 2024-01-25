from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
# Create your views here.

def register(request):
    if request.method == 'POST': 
        register_form = forms.RegistrationForm(request.POST) 
        if register_form.is_valid(): 
            register_form.save() 
            messages.success(request, 'Account created successfully')
            return redirect('login') 
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
                return redirect('profile')
        else:
            messages.warning(request, 'Login information incorrect')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html',{'form':form,'type':'Login'})


@login_required
def profile(request):
    post = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data':post})
    
def update_profile(request):
    if request.method == 'POST': 
        form = forms.ChangeUserData(request.POST, instance=request.user) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'Profile updated!')
            return redirect('profile') 
    else: 
        form = forms.ChangeUserData(instance=request.user) 
        return render(request, 'update_profile.html',{'form':form})

def password_change(request):
    if request.method == 'POST': 
        form = PasswordChangeForm(user=request.user, data=request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'Password changed successfully')
            update_session_auth_hash(request, form.user)
            return redirect('login')  
    else: 
        form = PasswordChangeForm(user=request.user) 
        return render(request, 'password_change.html',{'form':form})