from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta,datetime
import numpy as np

class User(AbstractUser):
    
    # *************datos personales ***********
    email = models.EmailField(_('enmail adrees'),unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    password = models.CharField(_('password'), max_length=128,blank=True,null=True)
    edad=models.IntegerField(null=True,blank=True)
    first_name = models.CharField(max_length=30)
    imagen_perfil = models.ImageField(upload_to='perfil/',blank=True,null=True)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    second_name = models.CharField(max_length=30,blank=True,null=True)
    fecha_nac = models.DateField(null=True,blank=True)   
    telefono_particular = models.CharField(max_length=100,blank=True,null=True)
    facebook = models.CharField(max_length=150, unique=False, blank=True, null=True)
    gmail = models.CharField(max_length=150,blank=True, null=True)
    twitter = models.CharField(max_length=150,blank=True, null=True)
    github = models.CharField(max_length=150,blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    
    
    
   
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return  self.first_name + ' ' + self.last_name + ' - ' + self.email  + ' ' + str(self.id)
    


    

    
    

        
    


