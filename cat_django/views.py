'''
Created on 9 mars 2013

@author: paraita
'''
from django.http import HttpResponse
from django.shortcuts import render
from cat_django.models import Enigme

def enigme(request):
    _id = request.GET.get("id", "-1")
    if _id is "-1":
        return HttpResponse("pas bon")
    else:
        e = Enigme.objects.get(id_enigme=_id)
        params = {}
        params['enigme'] = e
        return render(request, 'base.html', params)