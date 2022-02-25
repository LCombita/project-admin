from django import forms
from .models import Reparto
from django.http import HttpResponse

class RepartoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hoja_ruta'].widget.attrs.update({'class': 'form-control', 'readonly':'True'})
        self.fields['anio_escritura'].widget.attrs.update({'class': 'form-control', 'readonly':'True'})
        self.fields['proyecto'].widget.attrs.update({'class': 'form-control'})
        self.fields['acto_juridico'].widget.attrs.update(
            {'class': 'form-control select2', 'data-placeholder':'Selecione los actos jurídicos.'})
        self.fields['fecha_reparto'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})
        self.fields['escritura'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_escritura'].widget.attrs.update(
            {'class': 'form-control', 'readonly':'True'})

    class Meta:
        model = Reparto
        fields = ['hoja_ruta', 'anio_escritura', 'proyecto', 'acto_juridico',
         'fecha_reparto', 'escritura', 'fecha_escritura', 'activo']
        labels = {
            'escritura':'', 'fecha_escritura':'', 'fecha_reparto':'',
            'activo':'', 'proyecto':'', 'acto_juridico':'', 'hoja_ruta':'', 'anio_escritura':'' 
            }
        help_texts = {
            'proyecto': 'Seleccione el proyecto relacionado con el trámite.',
            'acto_juridico': 'Seleccione el acto relacionado. Si son varios, presion la tecla CTRL y seleccione los actos.',
            'fecha_escritura': 'Seleccione la fecha de la escritura.',
            'fecha_reparto': 'Seleccione la fecha de registro de la Hoja de Ruta.',
            'escritura': 'Digite el número de la escritura.',
            'hoja_ruta': 'Hoja de Ruta.',
            'anio_escritura': 'Número de escritura.',
            'activo': ' Activo. Desmarque esta opción si se anula el reparto.'
            }
 
    def clean(self):
        """Validar que el anio_escritura generado NO exista en la base de datos"""

        cleaned_data = super().clean()
        fecha_escritura = cleaned_data.get("fecha_escritura")
        escritura = cleaned_data.get("escritura")
        ae = fecha_escritura.strftime('%Y') + '-' + escritura
        if Reparto.objects.filter(anio_escritura=ae).exists():
            raise forms.ValidationError("La escritura ya existe, verificar el número.")
