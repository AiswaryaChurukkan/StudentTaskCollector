from django.contrib import admin
from .models import Student,Task,Course,Days

# # Register your models here.



class StudentsAdmin(admin.ModelAdmin):
    list_display=('Name','Course','Days','task','logo_image')

admin.site.register(Student, StudentsAdmin)

admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Days)