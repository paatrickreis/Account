from django import forms
from .models import Conta, Cliente

class UploadOFXForm(forms.Form):
    conta = forms.ModelChoiceField(queryset=Conta.objects.all())
    mes = forms.IntegerField(min_value=1, max_value=12)
    ano = forms.IntegerField(min_value=2000)
    arquivo = forms.FileField(label='Selecione um arquivo OFX')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cnpj']

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['cliente', 'tipo', 'banco', 'agencia', 'numero']