from django import forms
from .models import Issue


class CreateNewIssue(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('type', 'title', 'description', 'priority', 'status', 'finish_date', 'start_date')
