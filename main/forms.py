from .models import CompanyDB
from django.forms import ModelForm, TextInput, Textarea


class CompanyDBForm(ModelForm):
    class Meta:
        model = CompanyDB
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            })
        }
