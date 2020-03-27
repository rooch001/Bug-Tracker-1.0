from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    employeeId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField(verbose_name="age")
    mobile = models.CharField(max_length=13)
    jobTitle = models.CharField(max_length=15) 
    email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName + " " + self.lastName
