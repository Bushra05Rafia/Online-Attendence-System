from django.db import models

# Create your models here.

class addclass(models.Model):
    Course_code =models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    semister = models.CharField(max_length=100)
    startid =models.IntegerField(default=1)
    endid = models.IntegerField(default=1)


