# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import simplejson

def json_able(function):
    def _json_able(request, *args, **kwargs):
        function_response = function(request, *args, **kwargs)
        # A JSON response is requested
        if (request.META["HTTP_ACCEPT"].find('application/json') != -1):
            response = HttpResponse(mimetype='application/json')
            status = True
            if function_response.get('POODDING_STATUS', 'success') == 'error':
                status = False
            response.write(simplejson.dumps({'success': status, 'html': function_response.content}))
            return response
        return function_response
    return _json_able

def paginable(function):
    def _paginable(request, *args, **kwargs):
        try:
            page = int(request.GET.get('p', '1'))
            if page <= 0:
                page = 1
        except ValueError:
            page = 1
        try:
            items_per_page = int(request.GET.get('n', '10'))
            if items_per_page <= 0:
                items_per_page = 1
        except ValueError:
            items_per_page = 10
        return function(request, pagination={'page':page, 'items_per_page': items_per_page}, *args, **kwargs)
    return _paginable

def author_required(function):
    def _author_required(request, model, *args, **kwargs):
        if(model.author == request.user):
            return function(request, model, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return _author_required

def author_blocked(function):
    def _author_blocked(request, model, *args, **kwargs):
        if(model.author != request.user):
            return function(request, model, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return _author_blocked

def owner_required(function):
    def _owner_required(request, model, *args, **kwargs):
        if(model.owner == request.user):
            return function(request, model, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return _owner_required

def owner_blocked(function):
    def _owner_blocked(request, model, *args, **kwargs):
        if(model.owner != request.user):
            return function(request, model, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return _owner_blocked
