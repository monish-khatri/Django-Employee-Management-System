from tokenize import group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from employee.forms import EmployeeForm,UserForm,UserUpdateForm,EmployeeTeamForm
from employee.models import Employee,Team
from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.core.cache import cache
from django.views.generic.base import TemplateView
import secrets


class EmployeeView(View):
    http_method_names = ['get', 'post', 'put', 'delete']
    is_edit = False

    def dispatch(self,request, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(request, *args, **kwargs)
        if method == 'delete':
            return self.delete(request, *args, **kwargs)
        return super(EmployeeView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.is_edit:
            id = self.kwargs['id']
            employee = Employee.objects.get(id=id)
            if employee.team is not None:
                team = Team.objects.get(name=employee.team)
                # Convert modal instance to json format
                jsonObject = serializers.serialize('json', [ employee , team])
            else:
                jsonObject = serializers.serialize('json', [ employee])

            return HttpResponse(jsonObject)
        else:
            employees = get_employees(request)
            return render(request,"index.html",employees)

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                # To Store logged in user in the database directly
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.date_of_birth = datetime.strptime(request.POST['date_of_birth'], '%d/%m/%Y') # to parse date from string
                obj.user = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
                obj.team = Team.objects.get(id=request.POST['team']) # Add an author field which will contain current user's id
                obj.save() # Save the final "real form" to the DB
                messages.success(request,'Employee Added Successfully!')
                return redirect('/employee')
            except:
                messages.error(request,form.errors)
                return redirect('/employee')
        else:
            messages.error(request,form.errors)
            return redirect('/employee')

    def put(self, request, *args, **kwargs):
        id = self.kwargs['id']
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,request.FILES, instance = employee)
        if form.is_valid():
            try:
                # To Store logged in user in the database directly
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.date_of_birth = datetime.strptime(request.POST['date_of_birth'], '%d/%m/%Y') # to parse date from string
                obj.team = Team.objects.get(id=request.POST['team']) # Add an author field which will contain current user's id
                obj.save() # Save the final "real form" to the DB
                messages.success(request,'Employee Updated Successfully!')
                return redirect('/employee')
            except:
                messages.error(request,'Something Went Wrong!')
                return redirect('/employee')
        else:
            messages.error(request,form.errors)
            return redirect('/employee')

    def delete(self, request, *args, **kwargs):
        str = self.kwargs['str']
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


class AdminView(View):
    http_method_names = ['get', 'post', 'put', 'delete']
    is_edit = False
    def dispatch(self,request, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if not request.user.is_superuser:
            messages.error(request,'You do not have access to this area. Contact your site administrator to obtain access.')
            return redirect('/login')
        if method == 'put':
            return self.put(request, *args, **kwargs)
        if method == 'delete':
            return self.delete(request, *args, **kwargs)
        return super(AdminView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.is_edit:
            id = self.kwargs['id']
            user = User.objects.get(id=id)
            # Convert modal instance to json format
            jsonObject = serializers.serialize('json', [user])
            return HttpResponse(jsonObject)
        else:
            admins = get_user(request)
            return render(request,"admins.html",admins)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                token = secrets.token_urlsafe(nbytes=32)
                link = settings.APP_URL+"magic-link/"+token
                cache.set(token, request.POST['email'], timeout=10 * 60)
                subject = 'Biztech: Welcome to Employee Management System'
                message = ("Your Account Detail:\nUsername:{}\nPassword:{}\nLogin Url:{}\nOR\nYou Can Login Using Magic Link:{}").format(request.POST['username'],request.POST['password1'],settings.APP_URL,link)
                send_mail(subject,message,'emp@int.biztechcs.com',[request.POST['email']],fail_silently=False)
                messages.success(request,'User Added Successfully!')
                return redirect('/employee/admins')
            except:
                messages.error(request,form.errors)
                return redirect('/employee/admins')
        else:
            messages.error(request,form.errors)
            return redirect('/employee/admins')

    def put(self, request, *args, **kwargs):
        id = self.kwargs['id']
        user = User.objects.get(id=id)
        form = UserUpdateForm(request.POST,instance = user)
        if form.is_valid():
            try:
                if id == request.user.id and (not request.POST.get('is_superuser',False) or not request.POST.get('is_active',False)):
                    messages.info(request, 'Cannot update role or status cause you\'re logged in with this user')
                else:
                    form.save()
                    messages.success(request,'User Updated Successfully!')
                return redirect('/employee/admins')
            except:
                messages.error(request,'Something Went Wrong!')
                return redirect('/employee/admins')
        else:
            users = get_user(request)
            return render(request,"admins.html",users)

    def delete(self, request, *args, **kwargs):
        str = str.rstrip(',')
        idList = [int(x) for x in str.split(',')]
        idList.sort(reverse=True)
        lastAdminDelete = 0
        for id in idList:
            user = User.objects.get(id=id)
            if user.id != request.user.id:
                user.delete()
            else:
                lastUserName = user.get_full_name()
                lastAdminDelete+=1
                continue

        if lastAdminDelete !=0 and len(idList)>1:
            messages.info(request,"Cannot delete \"{}\" because it's the logged in user".format(lastUserName))
            messages.success(request,'Users Deleted Successfully!')
        elif len(idList) == 1 and lastAdminDelete !=0:
            messages.info(request,"Cannot delete \"{}\" because it's the logged in user".format(lastUserName))
        else:
            messages.success(request,'Users Deleted Successfully!')
        return redirect('/employee/admins')


class TeamView(View):
    http_method_names = ['get', 'post', 'put', 'delete']
    is_edit = False

    def dispatch(self,request, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(request, *args, **kwargs)
        if method == 'delete':
            return self.delete(request, *args, **kwargs)
        return super(TeamView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.is_edit:
            id = self.kwargs['id']
            team = Team.objects.get(id=id)
            jsonObject = serializers.serialize('json', [ team ])
            return HttpResponse(jsonObject)
        else:
            teams = get_teams(request)
            return render(request,"teams.html",teams)

    def post(self, request, *args, **kwargs):
        form = EmployeeTeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Team Added Successfully!')
            return redirect('/employee/teams')
        else:
            messages.error(request,form.errors)
            return redirect('/employee/teams')

    def put(self, request, *args, **kwargs):
        id = self.kwargs['id']
        team = Team.objects.get(id=id)
        form = EmployeeTeamForm(request.POST,instance = team)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Team Updated Successfully!')
                return redirect('/employee/teams')
            except:
                messages.error(request,'Something Went Wrong!')
                return redirect('/employee/teams')
        else:
            teams = get_teams(request)
            return render(request,"teams.html",teams)

    def delete(self, request, *args, **kwargs):
        str = self.kwargs['str']
        str = str.rstrip(',')
        idList = [int(x) for x in str.split(',')]
        for id in idList:
            team = Team.objects.get(id=id)
            team.delete()
        messages.success(request,'Teams Deleted Successfully!')
        return redirect('/employee/teams')


class TeamEmployeeView(TemplateView):
    template_name = 'team_employee.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TeamEmployeeView, self).get_context_data(*args, **kwargs)
        if self.request.method == 'GET':
            self.request.session['previousUrl'] = self.request.META.get('HTTP_REFERER')
            previousUrl = self.request.session.get('previousUrl')
        else:
            previousUrl = self.request.session.get('previousUrl')
        order_by = self.request.POST.get('order_by', '-id')
        searchName = self.request.POST.get('search','')
        id = self.kwargs['id']
        if self.request.user.is_superuser:
            teamEmployee = Employee.objects.filter(Q(team=id),Q(name__icontains =searchName) | Q(email__icontains =searchName)).order_by(order_by)
        else:
            teamEmployee = Employee.objects.filter(Q(user_id=self.request.user.id),Q(team=id),Q(name__icontains =searchName) | Q(email__icontains =searchName)).order_by(order_by)
        team = Team.objects.get(id=id)
        paginator = Paginator(teamEmployee, 5)
        page_number = self.request.GET.get('page',1)
        pageEmployee = paginator.get_page(page_number)
        pageEmployee.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        context = {'previousUrl':previousUrl,'team':team,'employees':pageEmployee,'totalRecords': len(teamEmployee),'order_by':order_by,'searchName':searchName}
        return context


class AboutUsView(TemplateView):
    template_name = 'about_us.html'
    def get_context_data(self, *args, **kwargs):
        context = super(AboutUsView, self).get_context_data(*args, **kwargs)
        return context


class ProfileView(TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        userProfile = User.objects.get(id=self.request.user.id)
        context = {'userProfile': userProfile}
        return context


def get_employees(request):
    if is_authenticated(request):
        order_by = request.GET.get('order_by', '-id')
        searchName = request.GET.get('search','')
        if request.user.is_superuser:
            employees = Employee.objects.filter(Q(email__contains=searchName) | Q(phone__icontains=searchName) | Q(name__icontains=searchName)| Q(team__name__icontains=searchName)| Q(user__username__icontains=searchName)).order_by(order_by)
        else:
            employees = Employee.objects.filter(Q(user_id=request.user.id),(Q(email__contains=searchName) | Q(phone__icontains=searchName) | Q(name__icontains=searchName))| Q(team__name__icontains=searchName)).order_by(order_by)
        paginator = Paginator(employees, 5)
        page_number = request.GET.get('page',1)
        pageEmployee = paginator.get_page(page_number)
        pageEmployee.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        return {'employees':pageEmployee,'totalRecords': len(employees),'EmployeeForm':EmployeeForm(),'UserForm':UserForm(),'order_by':order_by,'searchName':searchName}
    else:
        return redirect('/login')


def is_authenticated(request):
    if request.user.is_authenticated:
        request.session.modified = True
        return True
    else:
        return False


def get_user(request):
    if is_authenticated(request):
        order_by = request.GET.get('order_by', '-id')
        searchName = request.GET.get('search','')
        admins = User.objects.filter(Q(email__contains=searchName) | Q(username__icontains=searchName) | Q(first_name__icontains=searchName) | Q(last_name__icontains=searchName)).order_by(order_by)

        paginator = Paginator(admins, 5)
        page_number = request.GET.get('page',1)
        pageAdmin = paginator.get_page(page_number)
        pageAdmin.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        return {'admins':pageAdmin,'totalRecords': len(admins),'UserForm':UserForm(),'UserUpdateForm':UserUpdateForm(),'order_by':order_by,'searchName':searchName}
    else:
        return redirect('/login')


def get_teams(request):
    if is_authenticated(request):
        order_by = request.GET.get('order_by', 'name')
        searchName = request.GET.get('search','')
        teams = Team.objects.filter(name__icontains=searchName).order_by(order_by)
        paginator = Paginator(teams, 5)
        page_number = request.GET.get('page',1)
        pageTeams = paginator.get_page(page_number)
        pageTeams.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
        return {'teams':pageTeams,'totalRecords': len(teams),'EmployeeTeamForm':EmployeeTeamForm(),'order_by':order_by,'searchName':searchName}
    else:
        return redirect('/login')