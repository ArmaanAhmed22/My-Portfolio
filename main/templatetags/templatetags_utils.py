from django import template

register = template.Library()

@register.filter
@register.simple_tag
def define(the_value):
    return the_value

@register.filter
def addstr(arg1, arg2):
    return str(arg1) + str(arg2)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)