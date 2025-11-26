from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["job_title", "phone"]
    template_name = "accounts/profile_form.html"

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy("accounts:profile")
