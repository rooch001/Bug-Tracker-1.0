from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account

# Create your models here.


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    project_file = models.FileField(upload_to='files/project_file/',null=True)
    additional_file = models.FileField(upload_to='files/additional_file/',null=True)
    date_of_initiation = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return self.project_name + "-" + str(self.project_id)


class Member_Mapping(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
