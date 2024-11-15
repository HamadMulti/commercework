# ecommerce/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def split_first(value):
    """Splits the string and returns the first word."""
    if value:
        return value.split(" ")[0]
    return value
