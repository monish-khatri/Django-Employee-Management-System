from struct import pack_into
from django import forms

class DestinationForm(forms.Form):
    # each field would be mapped as an input field in HTML
    name = forms.CharField(label="Name",max_length=100, min_length=10,required=True,widget=forms.TextInput(attrs={"class":"class-1 class-2"}))
    image = forms.ImageField(allow_empty_file=True,required=False)
    desc = forms.CharField(max_length=500,widget=forms.Textarea())
    price = forms.IntegerField(max_value=5000,min_value=500,required=True)
    offer = forms.BooleanField(required=False)