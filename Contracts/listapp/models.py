from django.db import models

# Create your models here.


class Contract(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
