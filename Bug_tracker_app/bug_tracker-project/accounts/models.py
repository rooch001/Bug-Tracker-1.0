from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    emp_id      = models.AutoField(primary_key=True)
    first_name  = models.CharField(max_length=30)
    last_name   = models.CharField(max_length=30)
    age         = models.IntegerField()
    mobile      = models.CharField(max_length=13)
    job_title   = models.CharField(max_length=15)
    email       = models.ForeignKey(User, on_delete=models.CASCADE)
    photo       = models.ImageField(upload_to='images/photos/')
    address     = models.TextField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name
