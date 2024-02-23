from django import forms
from .models import Furnitures

class FurnituresForm(forms.ModelForm):
    class Meta:
        model = Furnitures
        fields = '__all__'