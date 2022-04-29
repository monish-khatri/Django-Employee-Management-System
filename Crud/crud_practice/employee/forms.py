from django import forms
from employee.models import Employee

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