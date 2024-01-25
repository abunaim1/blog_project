from django.shortcuts import render
from django.shortcuts import render, redirect
from post.forms import PostForm
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post.instance.author = request.user
            post.save()
            return redirect('home')
    else:
        post = PostForm()

    return render(request, 'add_post.html', {'form':post})

def edit_post(request, id):
    post_ob = models.Post.objects.get(pk=id)
    post = PostForm(instance=post_ob)
    if request.method == 'POST':
        post = PostForm(request.POST, instance=post_ob)
        if post.is_valid():
            post.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form':post})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
