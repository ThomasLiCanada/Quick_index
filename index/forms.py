
from django import forms
from .models import Index


class InputIndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['key_words',
                  'address',
                  ]