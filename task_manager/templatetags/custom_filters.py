from django import template
from django.utils.html import strip_tags


register = template.Library()


@register.filter
def removetagsbr(value):
    return strip_tags(value.replace('<br>', ''))