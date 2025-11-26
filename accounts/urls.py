from django.urls import path
from django.contrib.auth import views as auth_views

from .views import ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]
