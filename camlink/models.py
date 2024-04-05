from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.
class Link(models.Model):
  number = models.IntegerField(default=0)

class Video(models.Model):
    file = models.FileField(upload_to='videos/')
    uploaded_by = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    