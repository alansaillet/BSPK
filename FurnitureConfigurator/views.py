from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .models import Furniture
from .forms import FurnituresForm

import cadquery as cq

from FurnitureConfigurator.CAD_generator import generateShape

def home(request):
    form = FurnituresForm(request.POST or None)
    context = {'form': form, 'gltf_url': ""}

    if request.method == "POST":
        form = FurnituresForm(request.POST)
        if form.is_valid():
            #form.save()

            relative_gltf_path = generateShape(form.cleaned_data['length'],form.cleaned_data['width'],form.cleaned_data['height'])
            full_gltf_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{relative_gltf_path}")

            context['gltf_url'] = full_gltf_url

            messages.success(request, 'Your form has been saved successfully!')
        else:
            print(form.errors)  # Print errors to console
            messages.error(request, 'Error saving form.')
    else:
        context = {"form": FurnituresForm(), 'gltf_url': ""}  # No form submitted yet, provide a new blank form

    return render(request, 'home.html', context)