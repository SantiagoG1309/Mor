from django import forms
from .models import Recuerdo, MensajeEspecial, Foto, Musica, Sorpresa

class FechaAniversarioForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        # Convertir la fecha a formato string para comparar
        fecha_str = fecha.strftime('%d/%m/%Y') if fecha else ''
        if fecha_str != '20/11/2024':
            raise forms.ValidationError('Fecha incorrecta. Inténtalo de nuevo.')
        return fecha

class RecuerdoForm(forms.ModelForm):
    class Meta:
        model = Recuerdo
        fields = ['titulo', 'descripcion', 'fecha', 'imagen']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class MensajeEspecialForm(forms.ModelForm):
    class Meta:
        model = MensajeEspecial
        fields = ['titulo', 'contenido', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'contenido': forms.Textarea(attrs={'rows': 5}),
        }

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['titulo', 'descripcion', 'fecha', 'imagen', 'es_video']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'artista', 'archivo']

class SorpresaForm(forms.ModelForm):
    class Meta:
        model = Sorpresa
        fields = ['titulo', 'descripcion', 'activa']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }