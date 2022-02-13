from django import forms
from .models import Client


class CustumerFormClient(forms.ModelForm):
    name = forms.CharField(label='Nome')

    class Meta:
        model = Client
        fields = (
            'name',
        )
    