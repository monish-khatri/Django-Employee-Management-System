from tokenize import group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee.forms import EmployeeForm,UserForm,UserUpdateForm
from employee.models import Employee,EmployeeGroup
from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def employee(request):
    if is_authenticated(request):
        if request.method == "POST":
            form = EmployeeForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    # To Store logged in user in the database directly
                    obj = form.save(commit=False) # Return an object without saving to the DB
                    obj.user = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
                    obj.group = EmployeeGroup.objects.get(id=request.POST['group']) # Add an author field which will contain current user's id
                    obj.save() # Save the final "real form" to the DB
                    messages.success(request,'Employee Added Successfully!')
                    return redirect('/employee')
                except:
                    messages.error(request,form.errors)
                    return redirect('/employee')
        else:
            employees = get(request)
            return render(request,"index.html",employees)
    else:
        return redirect('/login')


def get(request):
    if is_authenticated(request):
        order_by = request.GET.get('order_by', '-id')
        if request.user.is_superuser:
            employees = Employee.objects.all().order_by(order_by)
        else:
            employees = Employee.objects.filter(user_id=request.user.id).order_by(order_by)
        paginator = Paginator(employees, 5)
        page_number = request.GET.get('page',1)
        pageEmployee = paginator.get_page(page_number)
        pageEmployee.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        return {'employees':pageEmployee,'totalRecords': len(employees),'EmployeeForm':EmployeeForm(),'UserForm':UserForm(),'order_by':order_by}
    else:
        return redirect('/login')


def edit(request, id):
    if is_authenticated(request):
        if request.method == "GET":
            employee = Employee.objects.get(id=id)
            group = EmployeeGroup.objects.get(name=employee.group)
            # Convert modal instance to json format
            jsonObject = serializers.serialize('json', [ employee , group])
            return HttpResponse(jsonObject)
        else:
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(request.POST,request.FILES, instance = employee)
            if form.is_valid():
                try:
                    # To Store logged in user in the database directly
                    obj = form.save(commit=False) # Return an object without saving to the DB
                    obj.user = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
                    obj.group = EmployeeGroup.objects.get(id=request.POST['group']) # Add an author field which will contain current user's id
                    obj.save() # Save the final "real form" to the DB
                    messages.success(request,'Employee Updated Successfully!')
                    return redirect('/employee')
                except:
                    messages.error(request,'Something Went Wrong!')
                    return redirect('/employee')
            else:
                employees = get(request)
                return render(request,"index.html",employees)
    else:
        return redirect('/login')


def delete(request, str):
    if is_authenticated(request):
        str = str.rstrip(',')
        idList = [int(x) for x in str.split(',')]
        try:
            for id in idList:
                employee = Employee.objects.get(id=id)
                employee.delete()
            messages.success(request,'Employees Deleted Successfully!')
            return redirect('/employee')
        except:
            messages.error(request,'Something Went Wrong!')
            return redirect('/employee')
    else:
        return redirect('/login')

def user_delete(request, str):
    if is_authenticated(request):
        str = str.rstrip(',')
        idList = [int(x) for x in str.split(',')]
        try:
            for id in idList:
                user = User.objects.get(id=id)
                user.delete()
            messages.success(request,'Users Deleted Successfully!')
            return redirect('/employee/users')
        except:
            messages.error(request,'Something Went Wrong!')
            return redirect('/employee/users')
    else:
        return redirect('/login')


def is_authenticated(request):
    if request.user.is_authenticated:
        request.session.modified = True
        return True
    else:
        return False

def user_register(request):
    if is_authenticated(request):
        if request.method == "POST":
            form = UserForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    subject = 'Biztech: Welcome to Employee Management System'
                    message = ("Your Account Detail:\nUsername:{}\nPassword:{}\nLogin Url:{}").format(request.POST['username'],request.POST['password1'],settings.APP_URL)
                    send_mail(subject,message,'emp@int.biztechcs.com',[request.POST['email']],fail_silently=False)
                    messages.success(request,'User Added Successfully!')
                    return redirect('/employee/users')
                except:
                    messages.error(request,form.errors)
                    return redirect('/employee/users')
        else:
            users = get_user(request)
            return render(request,"users.html",users)
    else:
        return redirect('/login')

def get_user(request):
    if is_authenticated(request):
        order_by = request.GET.get('order_by', '-id')
        users = User.objects.all().order_by(order_by)
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page',1)
        pageUser = paginator.get_page(page_number)
        pageUser.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        return {'users':pageUser,'totalRecords': len(users),'UserForm':UserForm(),'UserUpdateForm':UserUpdateForm(),'order_by':order_by}
    else:
        return redirect('/login')

def edit_user(request, id):
    if is_authenticated(request):
        if request.method == "GET":
            user = User.objects.get(id=id)
            # Convert modal instance to json format
            jsonObject = serializers.serialize('json', [user])
            return HttpResponse(jsonObject)
        else:
            user = User.objects.get(id=id)
            form = UserUpdateForm(request.POST,instance = user)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request,'User Updated Successfully!')
                    return redirect('/employee/users')
                except:
                    messages.error(request,'Something Went Wrong!')
                    return redirect('/employee/users')
            else:
                users = get_user(request)
                return render(request,"users.html",users)
    else:
        return redirect('/login')