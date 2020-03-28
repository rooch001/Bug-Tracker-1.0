from django.contrib import admin
from .models import Project
from .models import Member_Mapping

# Register your models here.
admin.site.register(Project)
admin.site.register(Member_Mapping)
