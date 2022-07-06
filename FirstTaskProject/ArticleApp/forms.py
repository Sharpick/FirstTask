from turtle import width
from unicodedata import name
from django import forms
 
class Article(forms.Form):
    title = forms.CharField(label="Название", max_length=40)
    content = forms.CharField(label="Контент", widget=forms.Textarea)
