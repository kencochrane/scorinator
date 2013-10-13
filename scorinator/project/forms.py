import re

from django import forms
from django.core.validators import URLValidator
from project.models import Project


class ProjectForm(forms.ModelForm):
    URL_PREFIX = 'https://github.com/'

    url_part = forms.CharField(label="Github URL", max_length=150)

    class Meta:
        model = Project
        exclude = ('date_added', 'last_update', 'slug', 'repo_url')

    def clean_url_part(self):
        """Currently limited to github for now"""
        if not re.search(r"^[\w\-_/]+$", self.cleaned_data['url_part']):
            raise forms.ValidationError(
                "Only digits, letters, -, _ and / allowed")
        complete_url = "{url_prefix}{url_part}".format(
            url_prefix=self.URL_PREFIX,
            url_part=self.cleaned_data['url_part']
        )
        URLValidator(complete_url)
        self.cleaned_data['repo_url'] = complete_url
        return self.cleaned_data['url_part']
