# from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog
from .models import Contact
from django.contrib import messages
from .forms import ContactForm, EditBlog
from django.shortcuts import render, redirect

def index(request):
    blogs = Blog.objects.all()
    params = {'blogData': blogs, 'count':len(blogs)}    
    return render(request, 'blog/index.html', params)

def viewblog(request, id):
    blogs = Blog.objects.get(blog_id=id)
    params = {'blogData': blogs}
    return render(request, 'blog/view.html', params)

def editblog(request, id):
    if request.method=='POST':
        blog_category = request.POST['blog_category']
        blog_title = request.POST['blog_title']
        blog_desc = request.POST['blog_desc']

        blog = Blog(blog_id=id, blog_category=blog_category, blog_title = blog_title, blog_desc = blog_desc)
        blog.save()
        messages.success(request, 'Blog Updated Successfully.')
        return redirect('/blog')
    else:
        blogs = Blog.objects.get(blog_id=id)
        params = {
                'blogData': blogs, 
                'formSkelton': EditBlog({
                        'blog_category': blogs.blog_category,
                        'blog_title': blogs.blog_title,
                        'blog_desc': blogs.blog_desc,
                    })
            }
        return render(request, 'blog/edit.html', params)

def removeblog(request, id):
    blogs = Blog.objects.get(blog_id=id)
    blogs.delete()
    messages.error(request, 'Blog Removed Successfully.')
    return redirect('/blog')

def contact(request):
    params = {"contactForm": ContactForm}
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(message) < 5:
            messages.error(request, 'Please provide valid details' )
            return render(request, 'blog/contact.html', params)
        else:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, 'Form Filled Successfully. Our Team Reach you soon.')
            return redirect("/blog/contact", params)
    else:
        return render(request, 'blog/contact.html', params)
