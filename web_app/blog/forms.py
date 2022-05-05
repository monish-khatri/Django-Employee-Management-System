from django import forms
from .models import Blog, Category, Tags

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
            if visible.name != 'blog_img':
                visible.field.widget.attrs['class'] = 'form-control'
                visible.field.widget.attrs['autocomplete'] = 'off'

        self.fields['blog_category'].error_messages.update({
            'required': 'Please Select Category for Blog',
        })
        
    class Meta:
        model = Blog
        fields = ('blog_category', 'blog_tags', 'blog_title', 'blog_desc', 'blog_img')

    catData = Category.objects.all().order_by('-id')
    tagData = Tags.objects.all().order_by('-id')
    blog_category = forms.ModelChoiceField(queryset=catData, widget=forms.Select(attrs={'class': "form-control"}), required=True)
    blog_tags = forms.ModelMultipleChoiceField(
        queryset=tagData,
        widget=forms.Select(attrs={
            'multiple':'true',
            'class': "form-control"
            }), 
        required=False
    )
    # blog_title = forms.CharField(label='Enter Blog Title', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    # blog_desc = forms.CharField(label='Enter Blog Descritpion', widget=forms.Textarea(attrs={'class': "form-control"}))
    blog_img = forms.ImageField(label='Select Blog Image', required=False)