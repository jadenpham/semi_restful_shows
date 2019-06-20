from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=55)
    released_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)