from django.contrib import admin
from .models import Direction, Group, Task
<<<<<<< HEAD:task/main_app/admin.py

=======
>>>>>>> 59497b7b0164bfa67bccc6bbd74a9fc79af02abd:config/main_app/admin.py
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
<<<<<<< HEAD:task/main_app/admin.py
    prepopulated_fields = {"slug": ("name",)}
=======
    prepopulated_fields = {"slug": ("name",)}
>>>>>>> 59497b7b0164bfa67bccc6bbd74a9fc79af02abd:config/main_app/admin.py
