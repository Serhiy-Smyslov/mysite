import re
from django import forms
from .models import News
from django.core.exceptions import ValidationError


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=70)
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5,
#     }))
#     category = forms.ModelChoiceField(queryset=News.objects.all())


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self): # check on begin of title on numbers
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры!')
        return title
