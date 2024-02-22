from django.shortcuts import render
from django.contrib import messages

from .models import Table
from .forms import TableForm, ChairForm, TypeSelectorForm

def home(request):
    if request.method == "POST":
        form = ChairForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form has been saved successfully!')
        else:
            print(form.errors)  # Print errors to console
            messages.error(request, 'Error saving form.')
    else:
        form =  ChairForm()
    return render(request, 'home.html', {"TypeSelectorForm":TypeSelectorForm,"form": form})