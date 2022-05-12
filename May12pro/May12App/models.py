
from django.db import models
from auditlog.registry import auditlog

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    fee=models.IntegerField()
    school=models.CharField(max_length=50)
class School(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    department=models.CharField(max_length=100)
    
auditlog.register(Student)
auditlog.register(School)
