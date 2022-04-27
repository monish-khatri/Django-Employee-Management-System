from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages


# Create your views here.
def is_authenticated(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def index(request):
    if is_authenticated(request):
        dests = Destination.objects.all()
        return render(request, "index.html", {'dests': dests})
    else:
        return redirect('accounts/login')

def details(request, id):
    if is_authenticated(request):
        details = Destination.objects.get(id=id)
        return render(request, "details.html", {'details': details})
    else:
        return redirect('accounts/login')

def add_destination(request):
    if is_authenticated(request):
        return render(request, "add_destination.html", {'DestinationForm':DestinationForm()})
    else:
        return redirect('accounts/login')

def add(request):
    if is_authenticated(request):
        form = DestinationForm(request.POST)
        try:
            form.save()
            messages.success(request,'Destination Added Successfully!')
            return redirect('/hello')
        except:
            messages.error(request,'Something Went Wrong!')
            return redirect('/')

    else:
        return redirect('accounts/login')