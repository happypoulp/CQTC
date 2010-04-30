from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def add_next(route):
    print route.path
    print dir(route)

