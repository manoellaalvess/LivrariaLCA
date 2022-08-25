from django import forms
from django.forms import fields
from .models import Crud

class CrudForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['description', 'price', 'quantity']