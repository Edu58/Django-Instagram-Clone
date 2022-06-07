from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='photos/')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()e

class Image(models.Model):
    image = models.ImageField(upload_to='photo/', blank=False, null=False)
    image_name = models.CharField(max_length=50, null=False, blank=False)
    image_caption = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateField(auto_now_add=True)
    reaction = models.IntegerField(default=0, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    
    class Meta:
        ordering = ['-created_on']
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.image_name


class Comments(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE,related_name="comments")
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class Likes(models.Model):
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, related_name='mylikes', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='photolikes', on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username

    def save_like(self):
        self.save()

    def delete_like(self):
        self.delete()
