from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  Escrituracion, Grantor, DataGrantor, Tramitador


class CreateGrantorForm(UserCreationForm):

    class Meta:
        model = Grantor
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name', 'last_name2', 'identification']


class UpdateGrantorForm(UserChangeForm):

    class Meta:
        model = Grantor
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name', 'last_name2', 'identification']


class DataGrantorForm(forms.ModelForm):
    
    class Meta:
        model = DataGrantor
        fields = ['phone', 'address']
        widgets = {
            'phone':forms.TextInput(attrs={
                'class':'form-control mb-2', 'placeholder':'número de teléfono'}),
            'address':forms.TextInput(attrs={
                'class':'form-control mb-2', 'placeholder':'dirección'}),
        }


#TRAMITADORES
class CreateTramitadorForm(UserCreationForm):

    class Meta:
        model = Tramitador
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name', 'last_name2', 'identification']


class UpdateTramitadorForm(UserChangeForm):

    class Meta:
        model = Tramitador
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name', 'last_name2', 'identification']


#ESCRITURACION
class CreateEscrituracionForm(UserCreationForm):

    class Meta:
        model = Escrituracion
        fields = [
            'username', 'email', 'password1', 'password2',
            'first_name', 'last_name', 'last_name2', 'identification']


class UpdateEscrituracionForm(UserChangeForm):

    class Meta:
        model = Escrituracion
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name', 'last_name2', 'identification']



"""
fields = '__all__'
fields = ['campo1', 'campo2']
exclude = ['campo1', 'campo2']
"""