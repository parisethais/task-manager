from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


PRIORITY_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
    ("urgent", "Urgent"),
]


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "task type"
        verbose_name_plural = "task types"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"
        URGENT = "urgent", "Urgent"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    task_type = models.ForeignKey("TaskType", on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_tasks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("is_completed", "deadline", "-created_at")

    def __str__(self) -> str:
        return self.name
