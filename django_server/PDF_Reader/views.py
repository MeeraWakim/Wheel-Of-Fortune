# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .forms import UploadFileForm

from django.shortcuts import render

# Create your views here.
def upload_pdf(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('<html><body>File successfuly uploaded </body></html')
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    for chunk in f.chunks():
        print chunk
