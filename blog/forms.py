from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='your text')
    text = forms.CharField(max_length=10, label='your text')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('text and name are same ', code='name_text')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your title',
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your title',
            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your title',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your title',
            })
        }
