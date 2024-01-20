from django.shortcuts import render, redirect
from profiles.forms import ProfileForm
# Create your views here.

def add_profile(request):
    if request.method == 'POST':
        identity = ProfileForm(request.POST)
        if identity.is_valid():
            identity.save()
            redirect('add_profile')
    else:
        identity = ProfileForm()
    return render(request, 'add_profile.html', {'form' : identity})