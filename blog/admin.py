from django.contrib import admin

# Register your models here
from .models import Blog, Category,Images

admin.site.register(Blog)

admin.site.register(Category)
admin.site.register(Images)
