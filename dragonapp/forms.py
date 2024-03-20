from django import forms
from dragonapp.models import Categories
from .models import Movies

class CategoryForm(forms.ModelForm):


    class Meta:
        model=Categories
        fields=['category']



class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['movie','poster','release_date','description','actors','category']
