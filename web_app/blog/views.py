# from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Tags
from .models import Contact
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import ContactForm, EditBlog
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

def handleSignin(request):
    if request.user.is_authenticated:
        redirect('/blog')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == '':
            messages.error(request,'Please enter username!')
            return render(request, 'login.html')
        if password == '':
            messages.error(request,'Please enter password!')
            return render(request, 'login.html')
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/blog/')
            else:
                messages.error(request,'Incorrect username or password!')
                return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/login.html')

def handleLogout(request):
    auth.logout(request)
    return redirect('/blog/login')

def handleSignup(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(email)<10:
            messages.error(request, " Your email is not valid")
            return render(request, 'blog/register.html')

        if len(fname)<2  or len(lname)<2:
            messages.error(request, " First,Last Name Should be proper")
            return render(request, 'blog/register.html')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return render(request, 'blog/register.html')

        myuser = User.objects.create_user(first_name=fname, last_name=lname, username=email, email=email, password=pass1)
        myuser.save()
        messages.success(request, "You are Registered successfully !")
        return redirect('/blog/login')
    else:
        return render(request, 'blog/register.html')

def index(request):
    page_number = request.GET.get('page')
    searchTitle = request.GET.get('searchTitle', '')
    searchCat = request.GET.get('searchCat', '')
    catData = Category.objects.all().order_by('-id')

    if searchTitle or searchCat:
        blogs = Blog.objects.filter(blog_title__icontains=searchTitle, is_published=1)
        if searchCat:
            blogs = Blog.objects.filter(
                blog_title__icontains=searchTitle,
                blog_category=searchCat,
                is_published=1
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
    if not request.user.is_authenticated:
        messages.error(request, "Please Login to Add/Update blog")
        return redirect('/blog/login')
        
    if request.method=='POST':
        blog_category = request.POST['blog_category']
        blog_tags = request.POST.getlist('blog_tags',[])

        form = EditBlog(request.POST, request.FILES)
        params = {
            'formSkelton': form,
            'action': "Add"
        }
        if form.is_valid():
            messages.success(request, 'Blog '+ request.POST['blog_title'] +' Successfully.')
            obj = form.save(commit=False)
            obj.blog_category = Category.objects.get(id=blog_category)
            if len(blog_tags)>0:
                tagsData = Tags.objects.filter(pk__in=blog_tags)
                for tagInstance in tagsData:
                    obj.blog_tags.add(tagInstance)

            obj.save()
            return redirect('/blog')
        else:
            messages.error(request, form.errors)
            return render(request, 'blog/edit.html', params)
    else:
        params = {'formSkelton': EditBlog(),'action': "Add"}
        return render(request, 'blog/edit.html', params)

def editblog(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Please Login to Add/Update blog")
        return redirect('/blog/login')

    if request.method=='POST':
        blog_category = request.POST['blog_category']
        blog_tags = set(request.POST.getlist('blog_tags'))
        blog_title = request.POST['blog_title']
        blog_desc = request.POST['blog_desc']
        is_published = request.POST['is_published']
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
        blog.is_published = is_published
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
                        'is_published': blogs.is_published
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
