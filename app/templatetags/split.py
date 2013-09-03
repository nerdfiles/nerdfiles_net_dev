from django import template
register = template.Library()


@register.filter(name='splitr')
def split(value, arg):
    return value.split(arg)
