# from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Tags
from .models import Contact
from django.contrib import messages
from .forms import ContactForm, EditBlog
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

def index(request):
    page_number = request.GET.get('page')
    searchTitle = request.GET.get('searchTitle')
    searchCat = request.GET.get('searchCat', '')
    catData = Category.objects.all().order_by('-id')

    if searchTitle or searchCat:
        blogs = Blog.objects.filter(blog_title__icontains=searchTitle).order_by('-blog_id')
        if searchCat:
            blogs = Blog.objects.filter(
                blog_title__icontains=searchTitle,
                blog_category=searchCat
            ).order_by('-blog_id')
    else:
        blogs = Blog.objects.all().order_by('-blog_id')

    paginator = Paginator(blogs, 10)
    page_obj = paginator.get_page(page_number)
    params = {
        'blogData': page_obj,
        'countCurrent': len(page_obj),
        'count':len(blogs),
        'catData':catData,
        'searchTitle':searchTitle,
        'searchCat':searchCat,
    }
    return render(request, 'blog/index.html', params)

def viewblog(request, id):
    blogs = Blog.objects.get(blog_id=id)
    tagCls = ['danger', 'warning', 'info', 'default', 'success']
    params = {
        'tagClass':tagCls,
        'blogData': blogs,
        'blogTags': blogs.blog_tags.all()
    }
    return render(request, 'blog/view.html', params)

def addblog(request):
    if request.method=='POST':
        blog_category = request.POST['blog_category']
    
        form = EditBlog(request.POST, request.FILES)
        params = {
            'formSkelton': form,
            'action': "Add"
        }
        if form.is_valid():
            messages.success(request, 'Blog '+ request.POST['blog_title'] +' Successfully.')
            obj = form.save(commit=False)
            obj.blog_category = Category.objects.get(id=blog_category)
            obj.save()
            return redirect('/blog')
        else:
            messages.error(request, form.errors)
            return render(request, 'blog/edit.html', params)
    else:
        params = {'formSkelton': EditBlog(),'action': "Add"}
        return render(request, 'blog/edit.html', params)

def editblog(request, id):
    if request.method=='POST':
        blog_category = request.POST['blog_category']
        blog_tags = set(request.POST.getlist('blog_tags'))
        blog_title = request.POST['blog_title']
        blog_desc = request.POST['blog_desc']
        blog = Blog.objects.get(blog_id=id)
        if request.FILES:
            blog_img = request.FILES['blog_img']
            
        # ---------------Method - 1 {For save form data}---------------
        # blog = Blog.objects.filter(blog_id=id, blog_category=blog_category, blog_title = blog_title, blog_desc = blog_desc)
        # blog.save()
        
        # ---------------Method - 2 {For save form data}---------------
        blog.blog_category=Category.objects.get(id=blog_category)
        tagsData = Tags.objects.filter(pk__in=blog_tags)
        blog.blog_tags.clear()
        for tagInstance in tagsData:
            blog.blog_tags.add(tagInstance)

        blog.blog_title = blog_title
        blog.blog_desc = blog_desc
        if request.FILES:
            blog.blog_img = blog_img
        blog.save()
        messages.success(request, 'Blog Updated Successfully.')
        return redirect('/blog')
    else:
        blogs = Blog.objects.get(blog_id=id)
        params = {
                'blogData': blogs,
                'action': "Edit",
                'blog_tags': blogs.blog_tags.values('id'),
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
