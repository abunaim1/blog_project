from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_author(request):
    if request.method == 'POST': #user post request koreche
        author_form = forms.AuthorForm(request.POST) #user er post request data ekhane capture korlam
        if author_form.is_valid(): #post kora data validitation check korlam
            author_form.save() # jodi data vlaid hoi taile database save korbo
            return redirect('add_author') # sob thik thakle soja ekhane chole jabe 
    else: # user normally website e blank form pabar jonne
        author_form = forms.AuthorForm() 
    return render(request, 'add_author.html' ,{'form' : author_form})