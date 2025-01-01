from django.contrib import admin

# Register your models here.
from .models import Category, Gallery

admin.site.register(Category)
admin.site.register(Gallery)