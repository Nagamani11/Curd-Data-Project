from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    experience = models.IntegerField()
    skill = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    roll_number = models.IntegerField(default=11)
