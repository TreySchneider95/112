from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }