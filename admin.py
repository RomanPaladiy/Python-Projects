from django.contrib import admin
# importing the class from the other file.
from .models import DjangoClasses
# Register your models here.

# adding the class to the site.
admin.site.register(DjangoClasses)
