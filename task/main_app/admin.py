from django.contrib import admin
from .models import Direction, Group, Task

# Register your models here.


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {"slug": ("name",)}