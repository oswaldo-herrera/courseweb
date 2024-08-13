from django import forms 
from django.db.models import Min,Max
from .models import VideoProductos,Audio,PDFDocument

from applications.users.models import User

        
class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoProductos
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }
        
class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'description', 'image', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }  
        
class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'file','image']  
        
        
        
        
        
        
        
        
        
   


    
