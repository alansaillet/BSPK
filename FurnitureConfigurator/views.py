from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .models import Furniture
from .forms import FurnituresForm

import cadquery as cq

from FurnitureConfigurator.CAD_generator import generateShape

def home(request):
    context = {"form": FurnituresForm()}

    if request.method == "POST":
        form = FurnituresForm(request.POST)
        if form.is_valid():
            form.save()
            relative_gltf_path = generateShape(form.cleaned_data['length'],form.cleaned_data['width'],form.cleaned_data['height'])
            messages.success(request, 'Your form has been saved successfully!')
            full_gltf_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{relative_gltf_path}")
            context['gltf_url'] = "media/tmp_60c9bbf6-b10f-4a5d-a4d6-6cf693b64f0a.gltf"
        else:
            print(form.errors)  # Print errors to console
            messages.error(request, 'Error saving form.')

    return render(request, 'home.html', context)