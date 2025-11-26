from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from .forms import ProfileForm
from .models import Profile


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        context["profile"] = profile
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
