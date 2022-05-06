from cProfile import label
from django import forms
from employee.models import Employee,EmployeeTeam
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm 
from django.core.exceptions import ValidationError  

class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            fieldClasses = 'form-control'
            visible.field.widget.attrs['class'] = fieldClasses


    class Meta:
        model = Employee
        fields = ['name', 'email','phone','image','date_of_birth','team']
    name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Name','id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address','id':'email'}),required=True)
    phone = forms.IntegerField(min_value=10000000,max_value=999999999999,required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone Number','id':'phone'}))
    image = forms.ImageField(allow_empty_file=True,required=False,widget=forms.FileInput(attrs={'id':'image'}))
    team = forms.ModelChoiceField(queryset=EmployeeTeam.objects.filter(status='1').order_by('name'), label='Select Team', widget=forms.Select(attrs={'class': "form-control","id":"team"}), required=True)
    date_of_birth = forms.DateField(required=True,widget=forms.TextInput(attrs={'id':'date_of_birth'}))


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' if visible.name != 'is_superuser' else ''
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2','is_superuser']

    username = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Username','id':'username'}))
    first_name = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'First Name','id':'first_name'}))
    last_name = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Last Name','id':'last_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address','id':'email'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','id':'password1'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','id':'password2'}),required=True)
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'is_superuser'}),required=False)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit = True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            is_superuser=self.cleaned_data['is_superuser']
        )
        return user

class UserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' if visible.name != 'is_superuser' and visible.name != 'is_active' else ''
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','is_superuser','is_active']

    username = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Username','id':'edit-username'}))
    first_name = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'First Name','id':'edit-first_name'}))
    last_name = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Last Name','id':'edit-last_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address','id':'edit-email'}),required=True)
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'edit-is_superuser'}),required=False)
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'edit-is_active'}),required=False)


class EmployeeTeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeTeamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = EmployeeTeam
        fields = ['name','status']

    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'name'}))
    status = forms.ChoiceField(choices=EmployeeTeam.STATUS,widget=forms.Select(attrs={'id':'status'}))