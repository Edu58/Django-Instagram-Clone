from django.contrib import admin
from .models import Profile, Comments

# Register your models here.
admin.site.register([Profile, Comments])
