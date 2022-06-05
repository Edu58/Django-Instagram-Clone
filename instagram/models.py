from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, null=False, blank=False)
