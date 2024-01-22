from django.shortcuts import render
from django.shortcuts import render, redirect
from post.forms import PostForm
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            redirect('add_post')
    else:
        post = PostForm()

    return render(request, 'add_post.html', {'form':post})