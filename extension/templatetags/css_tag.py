from django import template

register = template.Library()

# @register.inclusion_tag(None)
@register.inclusion_tag('extension/gravatar.html')
def css_tag(f):
    # print dir(css_tag)
    # print css_tag.func_closure
    # print css_tag.func_code
    # print css_tag.func_defaults
    # print css_tag.func_dict
    # print css_tag.func_doc
    # print css_tag.func_globals
    # print css_tag.func_name
    return {'css': f}

