from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee.forms import EmployeeForm
from employee.models import Employee
from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator


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
        employees = get(request)
        return render(request,"index.html",employees)

def get(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, 2)
    page_number = request.GET.get('page')
    pageEmployee = paginator.get_page(page_number)
    return {'employees':pageEmployee,'totalRecords': len(employees),'pageRecords':len(pageEmployee)}

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
            employees = get(request)
            return render(request,"index.html",employees)

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request,'Employee Deleted Successfully!')
    return redirect('/employee')