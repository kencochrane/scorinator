from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def display_score(value):
    try:
        fvalue = float(value)
        tag = "danger"
        title = "Poor"
        if fvalue >= 80.0:
            tag = "success"
            title ="Excellent"
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

    return mark_safe("<span class='label label-{tag} score' data-toggle='tooltip' title='{title}'>{score}</span>".format(
        score=value,
        tag=tag,
        title=title.capitalize())
    )
