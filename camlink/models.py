from django.db import models

# Create your models here.
class Link(models.Model):
  number = models.IntegerField(default=0)
