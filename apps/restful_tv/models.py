from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        title = Show.objects.filter(title=postData['title'])
        if len(title) > 0:
            errors['title'] = "Show already exist"
        elif len(postData['title'])<2:
            errors['title'] = "Show title should be at least 2 characters"
        elif len(postData['network'])<3:
            errors['network'] = "Show's network should be at least 3 characters"
        elif len(postData['description'])<10:
            errors['description'] = "Show's description must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=55)
    released_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()