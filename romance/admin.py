from django.contrib import admin
from .models import Recuerdo, MensajeEspecial, Foto, Musica, Sorpresa

# Registrar modelos en el panel de administración
admin.site.register(Recuerdo)
admin.site.register(MensajeEspecial)
admin.site.register(Foto)
admin.site.register(Musica)
admin.site.register(Sorpresa)
