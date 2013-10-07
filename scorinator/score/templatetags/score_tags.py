from django import template
from django.utils.safestring import mark_safe
from score.models import ProjectScore


register = template.Library()


@register.simple_tag()
def projects_scored():
    return ProjectScore.objects.graded()


@register.filter()
def display_project_score(value):
    try:
        fvalue = float(value)
        tag = "danger"
        title = "Poor"
        if fvalue >= 80.0:
            tag = "success"
            title = "Excellent"
        elif fvalue >= 70.0:
            tag = "info"
            title = "Very Good"
        elif fvalue >= 60.0:
            tag = "primary"
            title = "Good"
        elif fvalue >= 40.0:
            tag = "warning"
            title = "Needs Improvement"
    except (ValueError, TypeError):
        tag = "default"
        value = "?"
        title = "Calculating Score'"
    return display_score(value, tag, title)


@register.filter()
def display_attribute_score(value):
    tag = "default"
    title=""
    return display_score(value, tag, title)


def display_score(value, tag, title):
    return mark_safe(
        "<span class='label label-{tag} score' data-toggle='tooltip' "
        "title='{title}'>{score}</span>".format(
            score=value,
            tag=tag,
            title=title.capitalize()))
