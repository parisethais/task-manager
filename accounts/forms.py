from django import forms
from .models import Profile, JobTitle


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("job_title", "phone", "avatar")

    job_title = forms.ModelChoiceField(
        queryset=JobTitle.objects.all(),
        required=False,
        label="Job title",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    phone = forms.CharField(
        required=False,
        label="Phone",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    avatar = forms.ImageField(
        required=False,
        label="Avatar",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )
