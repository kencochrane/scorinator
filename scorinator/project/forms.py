from django import forms
from project.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('date_added', 'last_update')