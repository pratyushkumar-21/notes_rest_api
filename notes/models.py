from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length = 50)
    notes = models.FileField(upload_to='notes')
