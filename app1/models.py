from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    rollno =models.CharField(max_length=100)

# Create your models here.
