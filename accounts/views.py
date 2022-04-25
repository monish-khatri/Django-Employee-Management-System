from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

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
            return redirect('register')
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email address already in use!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email, first_name=first_name,last_name=last_name )
                user.save()
                messages.success(request, 'User Created Successfully')
                return redirect('login')
        else:
            messages.error(request,'Password & Confrim Password is not same!!!')
            return redirect('register')
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Incorrect username or password')
            return redirect('login')
    else:
        return render(request, "login.html")