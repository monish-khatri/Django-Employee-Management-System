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
            if visible.name == 'is_published':
                visible.field.widget.attrs['class'] = ''

        self.fields['blog_category'].error_messages.update({'required': 'Please select Category for Blog',})
        self.fields['blog_title'].error_messages.update({'required': 'Please add nice Title for Blog',})
        self.fields['blog_desc'].error_messages.update({'required': 'Please add eyecatching Description for Blog',})

    class Meta:
        model = Blog
        fields = ('blog_category', 'blog_tags', 'blog_title', 'blog_desc', 'blog_img', 'is_published')

    blog_category = forms.ModelChoiceField(
        required=True,
        queryset=Category.objects.all().order_by('-id'), 
        widget=forms.Select(attrs={'class': "form-control"}), 
    )
    blog_tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tags.objects.all().order_by('-id'),
        widget=forms.SelectMultiple(attrs={
            'multiple':'true',
            'class': "form-control"
            }), 
    )
    is_published = forms.ChoiceField(choices=[('1','Yes'),('0','No')], widget=forms.RadioSelect)
    # blog_title = forms.CharField(label='Enter Blog Title', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    # blog_desc = forms.CharField(label='Enter Blog Descritpion', widget=forms.Textarea(attrs={'class': "form-control"}))
    blog_img = forms.ImageField(label='Select Blog Image', required=False)