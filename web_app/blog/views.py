from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    params = {'blogData': blogs}
    return render(request, 'blog/index.html', params)

def viewblog(request, id):
    blogs = Blog.objects.get(blog_id=id)
    params = {'blogData': blogs}
    return render(request, 'blog/view.html', params)
