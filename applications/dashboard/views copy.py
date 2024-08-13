from django.forms import BaseModelForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views import View
from django.views.decorators.http import require_POST,require_GET
from django.db import IntegrityError
from django.http import HttpResponseBadRequest,HttpResponseForbidden, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator

import base64
from django.core.files.base import ContentFile

from django.views.generic import TemplateView
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.shortcuts import render,redirect,get_object_or_404

from django.urls import reverse_lazy,reverse
from django.template.loader import get_template
from django.http import FileResponse
from datetime import datetime
import locale

from .models import ImageYaab,VideoProductos,Audio,PDFDocument
from .forms import VideoForm,AudioForm,PDFUploadForm

from applications.users.models import User
from applications.users.mixins import ValidarPermisosMixin
from applications.users.forms import UserChangeForm

from mifiel import Document, Client

import uuid
import logging



# Create your views here.from django.views.generic.base import TemplateView
# class DashboardView(LoginRequiredMixin,CreateView):
#     model = SimuladorPrueba
#     template_name="dashboard/index.html"
#     form_class = SimPruebas #SimuladorForm
#     success_url = reverse_lazy('dashboard_app:index')
    
#     def form_valid(self, form):
#         # Asignar el usuario logeado al campo usuario_user antes de guardar
#         form.instance.usuario_user = self.request.user
#         form.instance.registro_creditos = False
#         response = super().form_valid(form)
        
#         if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
#             return JsonResponse({'success': True})
#         else:
#             return response


##### videos y audio ######    
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_app:video_catalog')
    else:
        form = VideoForm()
    return render(request, 'dashboard/upload_video.html', {'form': form})  

def video_catalog(request):
    query = request.GET.get('q')
    if query:
        videos = VideoProductos.objects.filter(title__icontains=query)
    else:
        videos = VideoProductos.objects.all().order_by('-id')

    paginator = Paginator(videos, 8)  # 8 videos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/video_catalog.html', {'page_obj': page_obj, 'query': query})

def audio_list(request):
    query = request.GET.get('q', '')
    audios = Audio.objects.all().order_by('-id')
    if query:
        audios = audios.filter(title__icontains=query)
    
    paginator = Paginator(audios, 8)  # 8 audios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'dashboard/audio_catalog.html', {'page_obj': page_obj, 'query': query})

def add_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_app:audio_list')
    else:
        form = AudioForm()
    return render(request, 'dashboard/add_audio.html', {'form': form})
##### videos y audio ######  
def pdf_list(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'dashboard/pdf_list.html', {'pdfs': pdfs})

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_app:pdf_list')
    else:
        form = PDFUploadForm()
    return render(request, 'dashboard/upload_pdf.html', {'form': form})

    
   
        
    
    
    
        
        
        
                
    
    
    
 

