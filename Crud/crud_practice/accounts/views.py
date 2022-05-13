from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as direct_login
from django.core.cache import cache
from django.views.decorators.http import require_GET
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']

        if first_name == '' or last_name == '' or username == '' or email == '' or password == '':
            messages.error(request,'All fields are required!')
            return render(request, 'register.html')
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email address already in use!')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username,password=password,email=email, first_name=first_name,last_name=last_name )
                user.save()
                """ uncomment below code to Redirect to Dashboard directly after registration
                new_user = authenticate(username=username,password=password)
                direct_login(request, new_user)"""
                messages.success(request, 'User Created Successfully')
                return redirect('/login')
        else:
            messages.error(request,'Password & Confrim Password is not same!!!')
            return render(request, 'register.html')
    else:
        return render(request, "register.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('/employee')
    else:
        if request.method == 'POST':

            username = request.POST.get('username','')
            password = request.POST.get('password','')
            if username == '':
                messages.error(request,'Please enter username!')
                return render(request, 'login.html')
            if password == '':
                messages.error(request,'Please enter password!')
                return render(request, 'login.html')
            else:
                remember_me = request.POST.get('remember','off')
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    if remember_me == 'on':
                        request.session.set_expiry(60*60*24*7)
                    return redirect('/employee/profile')
                else:
                    messages.error(request,'Incorrect username or password!')
                    return render(request, 'login.html')
        else:
            return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/login')

@require_GET
def login_with_magic_link(request,token):
    email = cache.get(token)
    if email is None:
        messages.error(request,'Magic Link invalid/expired')
        return redirect('/login')
    cache.delete(token)
    user, _ = User.objects.get_or_create(email=email)
    auth.login(request, user)
    return redirect("/employee/profile")