from django.db import models

# Create your models here.

class Notifications(models.Model):
    notification = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.notification[0:10]

class Associations(models.Model):
    name = models.CharField(max_length=250, null=False)
    image = models.ImageField(upload_to='Associations')

    def __str__(self):
        return self.name
    
class Memories(models.Model):
    title = models.CharField(max_length=250, null=False)
    video = models.FileField(upload_to='Memories')
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title