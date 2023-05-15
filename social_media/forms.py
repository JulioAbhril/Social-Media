from django import forms
from .models import SocialPost, SocialComment

class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border-gray-300 rounded-md',
            'rows': '3',
            'placeholder': 'Say Something...'
            }),
        required=True)

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={}),
        required=False
        )
    
    
    class Meta:
        model=SocialPost
        fields=['body']