from django.contrib import admin
from .models import Profile, JobTitle


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "job_title", "phone")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "job_title__name",
        "phone",
    )
