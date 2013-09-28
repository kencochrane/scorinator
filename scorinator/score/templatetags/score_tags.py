from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def display_score(value):
    tag = "danger"
    if float(value) >= 80.0:
        tag = "success"
    elif float(value) >= 70.0:
        tag = "info"
    elif float(value) >= 60.0:
        tag = "primary"
    elif float(value) >= 40.0:
        tag = "warning"
    return mark_safe("<span class='label label-{tag}'>{score}</span>".format(
        score=value,
        tag=tag)
    )