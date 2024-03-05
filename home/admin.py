from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','status']
    search_fields = ['title']
    list_filter = ['status']
    ordering = ('title', 'status')
    list_editable = ['status',]


