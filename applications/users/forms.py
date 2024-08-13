from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Group
from datetime import datetime
from .models import User
from django.utils.translation import gettext_lazy as _


# class SignaturePadWidget(forms.widgets.Widget):
#     template_name = 'users/widgets/signature_pad_widget.html'


#     class Media:
#         js = ('https://cdn.jsdelivr.net/npm/signature_pad@2.3.2/signature_pad.js',)

# class SignaturePadFormField(forms.CharField):
#     widget = SignaturePadWidget

class AdminUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                # h-75 rounded-pill ml-1
                'class': 'form-control ',
                'type': 'email',
                'placeholder': 'usuario@ejemplo.com',

            }
        )
    )

    username = forms.CharField(
        max_length=50,
        label="Usuario",

        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Usuario...',

            }
        )
    )

    password1 = forms.CharField(
        max_length=50,
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Contraseña',

            }
        )
    )

    password2 = forms.CharField(
        max_length=50,
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Confirmar contraseña',

            }
        )
    )

    validate_email = forms.BooleanField(
        label='',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class' : 'd-none'
            }
        )
    
    )

    class Meta:

        model = User
        fields = ('email', 'username', 'password1',
                  'password2', 'validate_email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data['validate_email']:
            user.is_active = True
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    # Define los campos que deseas incluir en el formulario

    email = forms.EmailField(
        label="Email",

        widget=forms.EmailInput(
            attrs={
                # h-75 rounded-pill ml-1
                'class': 'form-control ',
                'type': 'email',
                'placeholder': 'usuario@ejemplo.com',

            }
        )
    )

    password1 = forms.CharField(
        max_length=50,
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'contraseña',

            }
        )
    )

    password2 = forms.CharField(
        max_length=50,
        label="Contraseña",

        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'confirmar contraseña...',

            }
        )
    )

    first_name = forms.CharField(
        max_length=50,
        label="Usuario",

        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'nombres...',

            }
        )
    )

    last_name = forms.CharField(
        max_length=50,
        label="Usuario",

        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'primer apellido...',

            }
        )
    )

    second_name = forms.CharField(
        max_length=50,
        label="Usuario",

        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'segundo apellido...',

            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',
                  'first_name', 'last_name', 'second_name')


class UserChangeForm(forms.ModelForm):

    email = forms.CharField(
        max_length=50,
        label="Usuario",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Usuario...',

            }
        )
    )

    first_name = forms.CharField(
        max_length=50,
        label="Nombre",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Nombre...',

            }
        )
    )

    last_name = forms.CharField(
        max_length=50,
        label="Apellido",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Apellido...',

            }
        )
    )

    second_name = forms.CharField(
        max_length=50,
        label="Segundo Apellido",
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_second_name',
                'class': 'form-control ',
                'placeholder': 'Apellido...',

            }
        )
    )

    telefono_particular = forms.CharField(
        max_length=50,
        label="Teléfono particular",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Teléfono...',

            }
        )
    )

    fecha_nac = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'id': 'id_fecha_nac',
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'ingresa tu fecha de nacimiento'

            }
        )

    )


    imagen_perfil = forms.ImageField(
        required=False,
        label='Imagen de Perfil',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    facebook = forms.CharField(
        max_length=50,
        label="Ingresa tu link de facebook",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'URL...',

            }
        )
    )
    
    gmail = forms.CharField(
        max_length=50,
        label="Ingresa tu link de gmail",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'URL...',

            }
        )
    )
    twitter = forms.CharField(
        max_length=50,
        label="Ingresa tu link de twitter",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'URL...',

            }
        )
    )
    github = forms.CharField(
        max_length=50,
        label="Ingresa tu link de github",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'URL...',

            }
        )
    )
    
    descripcion = forms.CharField(
        label="Incluye una breve descripción de ti: ",
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2',
                'placeholder': 'descripción...',

            }
        )
    )
    

    

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'second_name', 'fecha_nac', 'telefono_particular','imagen_perfil','facebook','gmail','twitter','github','descripcion')



class AsignarRolForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), label="Usuario")
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), label="Grupo")






