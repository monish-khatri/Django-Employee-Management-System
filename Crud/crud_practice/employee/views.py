from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from django.contrib import messages

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
       employees = show()
       return render(request,"index.html",{'employees':employees})

def show():
    employees = Employee.objects.all()
    return employees


def edit(request, id):
    employee = Employee.objects.get(id=id)
    print(employee)
    return render(request,'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")