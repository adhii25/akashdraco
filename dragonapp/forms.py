from django import forms
from dragonapp.models import Categories, Movies
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):


    class Meta:
        model=Categories
        fields=['category']

class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['movie','poster','release_date','description','actors','category']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']