from django.db import models
from datetime import datetime
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    descrption = models.CharField(max_length=1000)