from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'category', 'tags', 'image', 'video']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }