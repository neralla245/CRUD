from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    college=models.CharField(max_length=20)
