from django.contrib import admin
from .models import Profile, Comments, Image, Likes

# Register your models here.
admin.site.register([
    Profile,
    Comments,
    Image,
    Likes
])
