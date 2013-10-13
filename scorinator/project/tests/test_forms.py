import pytest

from django import forms
from project.forms import ProjectForm


@pytest.fixture
def project_form():
    p = ProjectForm()
    p.cleaned_data = {}
    return p


class TestCleanURL():
    def test_simple(self, project_form):
        project_form.cleaned_data['url_part'] = 'user/project'
        r = project_form.clean_url_part()
        assert r == 'user/project'
        assert project_form.cleaned_data[
            'repo_url'] == 'https://github.com/user/project'

    def test_space(self, project_form):
        project_form.cleaned_data['url_part'] = 'user/ project'
        with pytest.raises(forms.ValidationError):
            project_form.clean_url_part()

    def test_unscore(self, project_form):
        project_form.cleaned_data['url_part'] = 'user/project-some_else'
        r = project_form.clean_url_part()
        assert r == 'user/project-some_else'
        assert project_form.cleaned_data[
            'repo_url'] == 'https://github.com/user/project-some_else'
