from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    course_id = models.CharField(max_length = 250,primary_key=True)
    course_name = models.CharField(max_length=250, null=False)
    category = models.ManyToManyField(Categories)

