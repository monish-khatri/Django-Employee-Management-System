from django import forms

class DestinationForm(forms.Form):
    # each field would be mapped as an input field in HTML
    name = forms.CharField(max_length=100, min_length=10,required=True)
    image = forms.ImageField(allow_empty_file=False)
    desc = forms.CharField(max_length=500)
    price = forms.IntegerField(max_value=5000,min_value=500,required=True)
    offer = forms.BooleanField(initial=False)