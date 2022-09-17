from django.contrib import admin
from .models import *

# Register your models here
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']


