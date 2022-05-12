from django.contrib import admin
from .models import Student,School


# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display=['name','fee','school']
class AdminSchool(admin.ModelAdmin):
    list_display=['name','city','department']
    
admin.site.register(Student,AdminStudent)
admin.site.register(School,AdminSchool)