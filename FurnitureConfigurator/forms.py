from django import forms
from .models import Table, Chair, TypeSelector

class TypeSelectorForm(forms.ModelForm):
    class Meta:
        model = TypeSelector
        fields = ["type"]

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'length', 'width', 'height', 'style']

class ChairForm(forms.ModelForm):
    class Meta:
        model = Chair
        fields = ['name', 'height', 'style']