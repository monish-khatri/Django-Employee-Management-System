from django import forms
from .models import Blog

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    name = forms.CharField(label='Enter Your Name', max_length=100)
    email = forms.CharField(label='Enter Your Email', max_length=100)
    phone = forms.CharField(label='Enter Your Mobile', max_length=10)
    message = forms.CharField(label='Enter Your Message', widget=forms.Textarea)

class EditBlog(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditBlog, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Blog
        fields = ('blog_category', 'blog_title', 'blog_desc', 'blog_img')

    CHOICES = (('1', 'Category 1'),('2', 'Category 2'),('3', 'Category 3'),('4', 'Category 4'))
    blog_category = forms.ChoiceField(choices=CHOICES, label='Select Blog Category', widget=forms.Select(attrs={'class': "form-control"}))
    # blog_title = forms.CharField(label='Enter Blog Title', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    # blog_desc = forms.CharField(label='Enter Blog Descritpion', widget=forms.Textarea(attrs={'class': "form-control"}))
    blog_img = forms.ImageField(label='Select Blog Image', required=False)