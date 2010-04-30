# -*- coding: utf-8 -*-
from urlparse import urljoin, urlparse

from django import template
from django import http
from django.core import urlresolvers
from django.conf import settings

register = template.Library()

""" Discover the breadcrumb
"""
def breadcrumb(context):
    request = context['request']
    uri = request.get_full_path()
    parse_result = urlparse(uri)
    if parse_result.params:
        if not parse_result.path.endswith('/'):
            uri = '%s/;%s' % (parse_result.path, parse_result.params)
    if not uri.endswith('/'):
        uri = uri + '/'
    breadcrumbs=[]
    urlconf = getattr(request, "urlconf", settings.ROOT_URLCONF)
    resolver = urlresolvers.RegexURLResolver(r'^/', urlconf)
    while uri:
        callback=None
        try:
            callback, callback_args, callback_kwargs = resolver.resolve(uri)
        except http.Http404:
            pass
        else:
            # No exception, let's create the breadcrumb
            bc = getattr(callback, 'breadcrumb', None)
            if bc is not None:
                if not isinstance(bc, basestring):
                    bc = bc(callback_args, callback_kwargs)
                bread = { 'uri' : uri, 'title': bc }
                breadcrumbs.append(bread)
            if (uri == '/'):
                uri = ''
        if uri == '':
            break
        else:
            uri = urljoin(uri, '..')
    breadcrumbs.reverse()
    return {'breadcrumbs' : breadcrumbs, 'bsize': len(breadcrumbs)}

register.inclusion_tag('extension/breadcrumb.html', takes_context=True)(breadcrumb)

