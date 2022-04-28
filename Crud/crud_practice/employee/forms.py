from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Employee
        fields = ['name', 'email','phone']
    name = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Name','id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address','id':'email'}),required=True)
    phone = forms.CharField(required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone Number','id':'phone'}))