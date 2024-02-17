from django.contrib import admin
from task.models import TaskModel
# Register your models here.

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id','taskTitle','taskDescription','is_completed']