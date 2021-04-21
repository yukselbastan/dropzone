from django import forms
from .models import (
        Post, 
    )

class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [
        'title',
        'notes',
        'category_1',
        'category_2',
        'category_3',
        'description',
        'price',
        'title_bold',
        'title_colored',
        'border',
        'keywords',
        ] 