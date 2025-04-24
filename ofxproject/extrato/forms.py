from django import forms
class UploadOFXForm(forms.Form):
    arquivo = forms.FileField(label='Selecione um arquivo OFX')
