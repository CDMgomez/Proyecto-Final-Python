from django import forms
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'class':'form-control'}),
            'receiver': forms.Select(attrs={'class':'form-select'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            # Exclude the current user from the receiver choices
            self.fields['receiver'].queryset = User.objects.exclude(pk=user.pk)
