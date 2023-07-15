from django import forms


class GeradorForm(forms.Forms):
    nlinhas = forms.CharField(max_length=100, required=True)
    tipo_dado = forms.CharField(max_length=100, required=True)

