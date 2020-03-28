from django.db import models
from accounts.models import Account
from dashboard.models import Project

# Create your models here.
class Bug(models.Model):
    bug_id              =   models.AutoField(primary_key=True)
    target_to           =   models.ForeignKey(Account, on_delete=models.CASCADE)
    project_id          =   models.ForeignKey(Project, on_delete=models.CASCADE)
    bug_description     =   models.TextField()
    bug_file            =   models.FileField(upload_to='bug/files/')
    bug_priority        =   models.CharField(max_length=15)
    deadline            =   models.DateField()
    reported_by         =   models.CharField(max_length=30)
