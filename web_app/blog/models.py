from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    cat_name = models.CharField(max_length=250)
    cat_status = models.IntegerField(default='1')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name

class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag_name = models.CharField(max_length=250)
    tag_status = models.IntegerField(default='1')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tags'

    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    blog_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    blog_title = models.CharField(max_length=250)
    blog_desc = models.TextField()
    blog_img = models.ImageField(upload_to="blog/images", default='untitled.png')
    blog_tags = models.ManyToManyField(Tags)
    is_published = models.IntegerField(default='0')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
    
    def clean(self):
        if self.blog_title:
            self.blog_title = self.blog_title.strip()
        if self.blog_desc:
            self.blog_desc = self.blog_desc.strip()
            
    @property
    def blog_with_cat(self):
        return self.blog_title

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Contact Form Filled by ' + self.name + "("  + self.email + ")"
"""
    Reference : https://docs.djangoproject.com/en/4.0/ref/models/fields/
"""
