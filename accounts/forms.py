from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']