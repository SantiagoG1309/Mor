from django.db import models
from django.utils import timezone

class Recuerdo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='recuerdos/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo

class MensajeEspecial(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.titulo

class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='fotos/')
    es_video = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='musica/')
    
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Sorpresa(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
