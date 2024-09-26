from django import forms
from .models import Inventario

class formCadastroUsuario(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Sobrenome", max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user = forms.CharField(label="Usuário", max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuario", max_length=40)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['num_inventario', 'denominacao', 'localizacao','sala', 'link_imagem']  