from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='photos/')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Image(models.Model):
    image = models.ImageField(upload_to='photo/', blank=False, null=False)
    image_name = models.CharField(max_length=50, null=False, blank=False)
    image_caption = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
