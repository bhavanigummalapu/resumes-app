from django.contrib import admin

# Register your models here.
from .models import resumus

class formadmin(admin.ModelAdmin):
    list_display = ['name','age','sex','exp','email','address','pic','document']


admin.site.register(resumus,formadmin)