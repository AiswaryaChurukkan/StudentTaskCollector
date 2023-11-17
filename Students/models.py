from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from PIL import Image
from django.utils.html import format_html
# Create your models here.
class Course(models.Model):
    course=models.CharField(max_length=45) 
    
    def __str__(self):
        return self.course
    
class Days(models.Model):
    day=models.CharField(max_length=25)
    def __str__(self):
        return self.day

class Task(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Days=models.ForeignKey(Days,on_delete=models.CASCADE)
    task=models.CharField(max_length=45)
    
    def __str__(self):
        return self.task
 

class Student(models.Model):
    Name=models.CharField(max_length=25)
    Days=models.ForeignKey(Days,on_delete=models.CASCADE)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    task=ChainedForeignKey(Task,
         chained_field="Course",
         chained_model_field="Course",
         show_all=False,
         auto_choose=True,
         sort=True)
    Logo = models.ImageField(upload_to='images')

    def logo_image(self):
        return format_html('<img src="{0}" style="width: 145px; height:45px;" />'.format(self.Logo.url))


    logo_image.allow_tags = True

    
    def __str__(self):
        return self.Name