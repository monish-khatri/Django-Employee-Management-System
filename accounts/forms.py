from django import forms
 
# creating a form
class RegistrationForm(forms.Form):
    name = forms.CharField(max_length = 100)
    image = forms.ImageField(upload_to = 'pics' )
    desc = forms.TextField()
    price = forms.IntegerField()
    offer = forms.BooleanField(default=False)
    created_at = forms.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = forms.DateTimeField(auto_now=True, auto_now_add=False)