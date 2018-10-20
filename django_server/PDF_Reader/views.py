# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def upload_pdf(request):
    return HttpResponse("<body><br>Hello</br></body>")
