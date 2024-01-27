from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from post.forms import PostForm, CommentForm
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
# Create your views here.

@login_required
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


#class based view (for create post)
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

@login_required
def edit_post(request, id):
    post_ob = models.Post.objects.get(pk=id)
    post = PostForm(instance=post_ob)
    if request.method == 'POST':
        post = PostForm(request.POST, instance=post_ob)
        if post.is_valid():
            post.instance.author = request.user
            post.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form':post})


#class based view (for edit post)
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')


#class based view (for delete post)
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

#class based view (for showing the details of every post)
class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object #post model er object ke ekhane rakhlam
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

