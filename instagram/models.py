from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default="https://images.unsplash.com/photo-1654786387184-f6e050c81edc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80", null=True, blank=True, upload_to='photos/')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='photo/', blank=False, null=False)
    image_name = models.CharField(max_length=50, null=False, blank=False)
    image_caption = models.CharField(max_length=100, blank=False, null=False)
    created_on = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
      
    @classmethod
    def search_by_name(cls, search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image

    def __str__(self):
        return self.image_name


class Comments(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()


class Likes(models.Model):
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.image_name
    
    
    def save_like(self):
        self.save()

    def delete_like(self):
        self.delete()
