from django.db import models

class Blog(models.Model):
    blog_id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(default='1')
    blog_category = models.IntegerField(default='1')
    blog_title = models.CharField(max_length=250)
    blog_desc = models.TextField()
    blog_img = models.ImageField(upload_to="blog/images", default='untitled.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Contact Form Filled by ' + self.name + "("  + self.email + ")"
"""
    Reference : https://docs.djangoproject.com/en/4.0/ref/models/fields/
"""
