from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(label="Full name", max_length=150, required=True)
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = Profile
        fields = ["full_name", "email", "phone"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        self.fields["full_name"].initial = (
            self.user.get_full_name() or self.user.username
        )
        self.fields["email"].initial = self.user.email

        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")

    def save(self, commit=True):
        profile = super().save(commit=False)

        full_name = self.cleaned_data["full_name"].strip()
        parts = full_name.split(" ", 1)
        self.user.first_name = parts[0]
        self.user.last_name = parts[1] if len(parts) > 1 else ""
        self.user.email = self.cleaned_data["email"]

        if commit:
            self.user.save()
            profile.user = self.user
            profile.save()

        return profile
