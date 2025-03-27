import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Recuerdo, Foto, Musica

@receiver(pre_delete, sender=Recuerdo)
def eliminar_archivo_recuerdo(sender, instance, **kwargs):
    # Verificar si el recuerdo tiene una imagen
    if instance.imagen and os.path.isfile(instance.imagen.path):
        # Eliminar el archivo físico
        os.remove(instance.imagen.path)

@receiver(pre_delete, sender=Foto)
def eliminar_archivo_foto(sender, instance, **kwargs):
    # Verificar si la foto tiene una imagen
    if instance.imagen and os.path.isfile(instance.imagen.path):
        # Eliminar el archivo físico
        os.remove(instance.imagen.path)

@receiver(pre_delete, sender=Musica)
def eliminar_archivo_musica(sender, instance, **kwargs):
    # Verificar si la música tiene un archivo
    if instance.archivo and os.path.isfile(instance.archivo.path):
        # Eliminar el archivo físico
        os.remove(instance.archivo.path)