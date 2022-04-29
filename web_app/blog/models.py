from django.db import models

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    cat_name = models.CharField(max_length=250)
    cat_status = models.IntegerField(default='1')
    created_at = models.DateTimeField(auto_now=True)

class Blog(models.Model):
    blog_id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(default='1')
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    blog_title = models.CharField(max_length=250)
    blog_desc = models.TextField()
    blog_img = models.ImageField(upload_to="blog/images", default='untitled.png')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
    
    @property
    def blog_with_cat(self):
        return self.blog_title + '- asdd'

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
