from django.http import HttpResponse
from django.utils.http import urlquote
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response

def indice1(request):
    return "indice1"
