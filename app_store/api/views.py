import json
from urllib2 import Request, urlopen, URLError

from django.shortcuts import render
from django.http import JsonResponse
from api import config

def index(request):
    return JsonResponse({'foo':'bar'})

def app(request, app_id, param1='London'):
    context = {}
    urls = config.APPS[app_id]
    # import pdb
    # pdb.set_trace()
    for index, url in enumerate(urls):
        name = config.NAMES[app_id]
        req = Request(url + param1)
        resp = json.loads(urlopen(req).read())
        context[name[index]] = resp
    return JsonResponse(context)
