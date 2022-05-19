from django.db import models
from django.urls import reverse

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):

    # fields of the model
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list')