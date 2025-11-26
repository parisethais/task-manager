from django.urls import path

from .views import ProfileDetailView, ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),
]
