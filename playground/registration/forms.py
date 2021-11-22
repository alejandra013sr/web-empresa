from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from .models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields=("username","email","password1","password2")

    def clean_email(self):
        email= self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['avatar','bio','link']
        widgets={
            'avatar':forms.ClearableFileInput(
                attrs={
                    'class':'form-control-file mt-3',
                }
            ), #es el campo de limpiar
            'bio': forms.Textarea(
                attrs={
                    'class':'form-control mt-3',
                    'rows':3,
                    'placeholder':'Biografia'
                }
            ),
            'link':forms.URLInput(
                attrs={
                    'class':'form-control mt-3',
                    'placeholder':'Enlace'
                }
            )
        
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caractacteres como maximo y debe ser valido.")

    class Meta:
        model = User
        fields=["email"]

    def clean_email(self):
        email= self.cleaned_data.get("email")
        #comprobar si ha cambiado
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email