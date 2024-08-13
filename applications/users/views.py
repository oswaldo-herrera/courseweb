from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from allauth.account.views import SignupView
import pandas as pd
import base64
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
import os
from django.conf import settings
from django.views.generic.edit import FormView
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView


from .mixins import ValidarPermisosMixin
from .models import User
from .forms import UserCreationForm, UserChangeForm,  AdminUserCreationForm,  AsignarRolForm

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import  Group
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods

import uuid
from django.db.models import Q


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.


class AdminRegisterView(FormView):
    template_name = 'users/listar-usuarios.html'
    form_class = AdminUserCreationForm
    success_url = reverse_lazy('lista_usuarios')

    def form_valid(self, form):
        # Guardar el formulario y redirigir al éxito si es válido
        form.save()
        return super().form_valid(form)




class RegistrarUsuario(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Obtenemos los datos del formulario
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']  # Obtenemos la contraseña

        # Creamos una instancia del modelo de usuario pero no la guardamos aún
        user = form.save(commit=False)
        # Usamos make_password para cifrar la contraseña antes de guardarla
        user.password = make_password(password)
        user.save()
        return super().form_valid(form)

class EditarUsuario(UpdateView):
    model = User
    template_name = 'users/editar-usuario.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('user_app:lista_usuarios_general')


class EliminarUsuarios(DeleteView):
    model = User
    template_name = 'users/eliminar-usuario.html'
    success_url = reverse_lazy('user_app:lista_usuarios_general')


    

class ListaUsuariosGeneral(FormView, ListView):
    template_name = 'users/listar-usuarios-clientes.html'
    context_object_name = 'lista'
    form_class = AdminUserCreationForm
    success_url = reverse_lazy('user_app:lista_usuarios_general')

    def get_queryset(self):
        # usuarios_admin = User.objects.filter(groups__name='Administrador General').order_by('-date_joined')
        # usuarios_cobranza = User.objects.filter(groups__name='Cobranza').order_by('-date_joined')
        # usuarios_trabajadores = usuarios_admin.union(usuarios_cobranza)
        # usuarios_sin_grupo = User.objects.exclude(id__in=usuarios_trabajadores.values_list('id', flat=True))
        #return usuarios_sin_grupo
        return User.objects.filter(id=self.request.user.id)

    def form_valid(self, form):
        # Guardar el formulario y redirigir al éxito si es válido
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['allUser'] = User.objects.all()
        return context

class SolicitudCheck(View):
    def post(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            user.solicitud = True
            user.save()
            return JsonResponse({'message': 'Solicitud marcada como true'})

        except User.DoesNotExist:
            return JsonResponse({'message': 'Solicitud no encontrada'}, status=404)


class ClientesAll(ListView):
    template_name = 'users/clientes.html'
    context_object_name = 'clientes'

    def get_queryset(self):

        cliente = User.objects.filter(solicitud=True)

        return cliente


class RegistrarUsuario(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualizar la sesión del usuario para mantener la sesión iniciada
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('dashboard_app:index')  # Redirigir a la página de perfil o donde desees después de cambiar la contraseña
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = PasswordChangeForm(request.user)
 
    return render(request, 'users/change_password.html', {'form': form})

