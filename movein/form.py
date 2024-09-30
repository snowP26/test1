from django import forms
from django.contrib.auth.models import User
from .models import *

class signupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    pw_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Tenant
        fields = ['Tenant_firstName', 'Tenant_lastName', 'Tenant_Email', 'Tenant_Phone', 'password', 'pw_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        pw_confirm = cleaned_data.get('pw_confirm')

        # Password Validation
        if password and pw_confirm and password != pw_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class announcementForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['Announce_header', 'Announce_body', 'Announce_image']

