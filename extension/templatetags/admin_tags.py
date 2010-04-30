from django import template
from poodding.settings import *

register = template.Library()

@register.inclusion_tag('extension/admin_scripts.html', takes_context=True)
def admin_scripts(context):
    request = context['request']
    scripts = []
    
    if DEBUG or request.user.is_staff:
        scripts.append('/statics/js/admin.js')
    
    return {'scripts': scripts}

