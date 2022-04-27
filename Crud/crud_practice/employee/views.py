from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee.forms import EmployeeForm
from employee.models import Employee
from django.contrib import messages
from django.core import serializers


# Create your views here.
def employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Employee Added Successfully!')
                return redirect('/employee')
            except:
                messages.error(request,'Something Went Wrong!')
                return redirect('/employee')
    else:
       employees = get()
       return render(request,"index.html",{'employees':employees})

def get():
    employees = Employee.objects.all()
    return employees

def edit(request, id):
    if request.method == "GET":
        employee = Employee.objects.get(id=id)
        # Convert modal instance to json format
        jsonObject = serializers.serialize('json', [ employee ])
        return HttpResponse(jsonObject)
    else:
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Employee Updated Successfully!')
                return redirect('/employee')
            except:
                messages.error(request,'Something Went Wrong!')
                return redirect('/employee')
        else:
            employees = get()
            return render(request,"index.html",{'employees':employees})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request,'Employee Deleted Successfully!')
    return redirect('/employee')