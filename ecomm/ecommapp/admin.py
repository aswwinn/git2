from django.contrib import admin
from ecommapp.models import category
from ecommapp.models import Products

# Register your models here.

admin.site.register(category)
admin.site.register(Products)