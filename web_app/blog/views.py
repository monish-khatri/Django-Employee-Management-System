# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Blog
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def index(request):
    blogs = Blog.objects.all()
    params = {'blogData': blogs}
    return render(request, 'blog/index.html', params)

def viewblog(request, id):
    blogs = Blog.objects.get(blog_id=id)
    params = {'blogData': blogs, 'count':len(blogs)}
    return render(request, 'blog/view.html', params)

def contact(request):
    params = {"contactForm": ContactForm}
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(message) < 5:
            messages.error(request, 'Please provide valid details' )
        else:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, 'Form Filled Successfully. Our Team Reach you soon.')
            return redirect("/blog/contact", params)
    else:
        return render(request, 'blog/contact.html', params)
