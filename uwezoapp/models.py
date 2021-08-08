from django.db import models
from datetime import datetime, timezone
from django.db.models.fields import DateField


class New(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
