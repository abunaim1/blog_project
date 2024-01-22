from django.shortcuts import render, redirect
from categories.forms import CategoryForm
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            redirect('add_category')
    else:
        category = CategoryForm()

    return render(request, 'add_category.html', {'form':category})