from django import forms
from author.models import Author
"""
when we are working with a class and we need add some extra charecteristics/attributes to this class then we will use Meta class.
"""
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['name', 'bio']
        # exclude = ['bio']