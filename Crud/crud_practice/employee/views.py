from traceback import print_tb
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
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                # form.save()
                print(form.save())
                exit()
                messages.success(request,'Employee Added Successfully!')
                return redirect('/employee')
            except:
                messages.error(request,form.errors)
                return redirect('/employee')
    else:
        employees = get(request)
        return render(request,"index.html",employees)

def get(request):
    employees = Employee.objects.all().order_by('-id')
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page',1)
    pageEmployee = paginator.get_page(page_number)
    pageEmployee.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
    return {'employees':pageEmployee,'totalRecords': len(employees),'pageRecords':len(pageEmployee),'EmployeeForm':EmployeeForm()}

def edit(request, id):
    if request.method == "GET":
        employee = Employee.objects.get(id=id)
        # Convert modal instance to json format
        jsonObject = serializers.serialize('json', [ employee ])
        print(jsonObject)
        return HttpResponse(jsonObject)
    else:
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,request.FILES, instance = employee)
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

def delete(request, str):
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