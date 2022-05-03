from cProfile import label
from django import forms
from employee.models import Employee,EmployeeGroup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  


class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            fieldClasses = 'form-control phone-class' if visible.name == 'phone' else 'form-control'
            visible.field.widget.attrs['class'] = fieldClasses


    class Meta:
        model = Employee
        fields = ['name', 'email','phone','image']
    name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Name','id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address','id':'email'}),required=True)
    phone = forms.IntegerField(min_value=10000000,max_value=999999999999,required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone Number','id':'phone'}))
    image = forms.ImageField(allow_empty_file=True,required=False,widget=forms.FileInput(attrs={'id':'image'}))
    group = forms.ModelChoiceField(queryset=EmployeeGroup.objects.all(), label='Select Team', widget=forms.Select(attrs={'class': "form-control","id":"group"}), required=True)


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ['first_name', 'email','last_name','username','password1','password2']

    username = forms.CharField(min_length=3,max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Username','id':'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address','id':'email'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','id':'password1'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','id':'password2'}),required=True)

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
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user