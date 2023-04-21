from django.db import models

# Create your models here.

class DiaryRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
