import urllib, hashlib
from django import template

register = template.Library()

@register.inclusion_tag('extension/gravatar.html')
def show_gravatar(user, size=48):
    default = "http://www.gravatar.com/avatar/3b3be63a4c2a439b013787725dfce802.jpg"
    url = "http://www.gravatar.com/avatar.php?d=identicon"
    url += urllib.urlencode({
        'gravatar_id': hashlib.md5(user.email).hexdigest(), 
        'd': 'identicon', 
        'default': default, 
        'size': str(size)
    })
    return {'gravatar': {'url': url, 'size': size, 'username': user.username}}

