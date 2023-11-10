from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

# after create thin Student model or Any model
# 1. run cmd "python manage.py makemigrations" this is for generate sql query then
# 2. run cmd "python manage.py migrate" then create automatically many tables