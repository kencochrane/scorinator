from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def display_score(value):
    tag = "danger"
    if value > 80:
        tag = "success"
    elif value > 70:
        tag = "info"
    elif value > 60:
        tag = "primary"
    elif value > 40:
        tag = "warning"
    return mark_safe("<span class='label label-{tag}'>{score}</span>".format(
        score=value,
        tag=tag)
    )