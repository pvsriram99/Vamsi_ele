from django.db import models

# Create your models here.
class users(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Mobile = models.IntegerField()
    Message = models.CharField(max_length=100)
