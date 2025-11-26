from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from tasks.views import TaskListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", include(("tasks.urls", "tasks"), namespace="tasks")),
    path("", TaskListView.as_view(), name="index"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
