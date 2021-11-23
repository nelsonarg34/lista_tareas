from django.contrib import admin
from . import models

# List Admin
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created', 'updated']
    list_filter = ['user', 'created', 'updated']


# Task Admin
@admin.register(models.Task)
class TasktAdmin(admin.ModelAdmin):
    list_display = ['parent_list', 'title', 'description', 'deadline',
                    'priority', 'completed', 'created', 'updated']
    list_filter = ['created', 'updated', 'completed']

