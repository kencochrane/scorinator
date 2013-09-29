from django import forms
from project.models import Project


class ProjectForm(forms.ModelForm):
    url = forms.URLField(label="Github URL")

    class Meta:
        model = Project
        exclude = ('date_added', 'last_update', 'slug', 'repo_url')
