from django import forms
from .models import Poll

class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = []  # or list only the fields you want to include

