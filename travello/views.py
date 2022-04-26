from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        dests = Destination.objects.all()
        return render(request, "index.html", {'dests': dests})
    else:
        return redirect('accounts/login')

def add_destination(request):
    return render(request, "add_destination.html", {'DestinationForm':DestinationForm()})