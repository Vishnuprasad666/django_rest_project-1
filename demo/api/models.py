from django.db import models

# Create your models here.

class Assignments(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    last_date=models.DateField()

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    adderss=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="Teachers_image")
    
class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    last_date=models.DateTimeField()
    status=models.CharField(max_length=30,default="Pending")