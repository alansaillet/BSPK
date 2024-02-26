from django.shortcuts import render
from django.contrib import messages

from .models import Furniture
from .forms import FurnituresForm

import cadquery as cq

from FurnitureConfigurator.CAD_generator import generateShape

def home(request):
    if request.method == "POST":
        form = FurnituresForm(request.POST)
        if form.is_valid():
            form.save()
            generateShape(form.cleaned_data['length'],form.cleaned_data['width'],form.cleaned_data['height'])
            messages.success(request, 'Your form has been saved successfully!')
        else:
            print(form.errors)  # Print errors to console
            messages.error(request, 'Error saving form.')
    else:
        form =  FurnituresForm()
    return render(request, 'home.html', {"form":form})