from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def display_score(value):
    try:
        fvalue = float(value)
        tag = "danger"
        if fvalue >= 80.0:
            tag = "success"
        elif fvalue >= 70.0:
            tag = "info"
        elif fvalue >= 60.0:
            tag = "primary"
        elif fvalue >= 40.0:
            tag = "warning"
    except ValueError:
        tag = "default"
        value = "?"

    return mark_safe("<span class='label label-{tag}'>{score}</span>".format(
        score=value,
        tag=tag)
    )
