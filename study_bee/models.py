from time import timezone
from django.db import models
from django.utils import timezone

class StudyPlan(models.Model):
    TYPE_CHOICES = [
        ('group', 'Group'),
        ('individual', 'Individual'),
    ]
    
    name = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='')
    subject = models.CharField(max_length=100, default='')
    date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=200, default='')
    description = models.TextField(default='')

