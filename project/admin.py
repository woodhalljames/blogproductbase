from django.contrib import admin
from .models import *

class Subscribe(admin.ModelAdmin): 
    list_display = ('email', 'created_date')