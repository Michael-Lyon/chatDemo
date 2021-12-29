from django.db import models
from django.db.models.expressions import Value
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class Messages(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=100000)

    def __str__(self):
        return f"{self.room} by {self.user}"
