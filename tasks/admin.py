from django.contrib import admin

from .models import Position, TaskType, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "task_type", "deadline", "is_completed", "priority")
    list_filter = ("is_completed", "priority", "task_type", "deadline")
    search_fields = ("name", "description")
    filter_horizontal = ("assignees",)
