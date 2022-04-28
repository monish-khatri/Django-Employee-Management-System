from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


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
        # process form data
        name = request.POST['name']
        image = request.POST.get('image','')
        if image != '':
            imagePath = 'pics/' + image
        else:
            imagePath = 'pics/NoImage.png'


        upload_file = request.FILES['image']
        fs = FileSystemStorage(location='media/pics/')
        image = fs.save(upload_file.name, upload_file)
        desc = request.POST['desc']
        price = request.POST['price']
        offer = True if request.POST.get('offer',False) == 'on' else False
        obj = Destination(name=name,image=imagePath,desc=desc,price=price,offer=offer)#gets new object
        #finally save the object in db
        obj.save()
        messages.success(request,'Destination Added Successfully!')
        return redirect('/')

    else:
        return redirect('accounts/login')