from django.db import models

# Create your models here.
class Project(models.Model):
    project_id          =   models.AutoField(primary_key=True)
    project_name        =   models.CharField(max_length=30)
    description         =   models.TextField()
    project_file        =   models.FileField(upload_to='files/project_file/')
    additional_file     =   models.FileField(upload_to='files/additional_file/')
    date_of_initiation  =   models.DateField()
    deadline            =   models.DateField()
