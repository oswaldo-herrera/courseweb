from django.db import models
from decimal import Decimal

from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail

from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import uuid





        
def send_email(to_email, subject, message):
    from_email = "yaab2023tech@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, 'vgit jdxe pgaj ufqy')
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    



class ImageYaab(models.Model):

    top_image = models.ImageField(
        upload_to='solicitud/', blank=True, null=True)

    class Meta:
        verbose_name = 'imagen_yaab'




class VideoProductos(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    youtube_id = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Extraer el ID de YouTube al guardar el modelo
        self.youtube_id = self.extract_youtube_id()
        super(VideoProductos, self).save(*args, **kwargs)
        
    def extract_youtube_id(self):
        import re
        pattern = r'(?:v=|be/)([^&/]+)'
        match = re.search(pattern, self.url)
        if match:
            return match.group(1)
        return None
    
class Audio(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='audio_images/', blank=True, null=True)
    file = models.FileField(upload_to='audio_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PDFDocument(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    file = models.FileField(upload_to='pdfs/')
    image = models.ImageField(upload_to='pdf_images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    