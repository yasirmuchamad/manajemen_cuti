from django import forms
from .models import *
from django.forms import DateTimeInput

class CutiForm(forms.ModelForm):
    """Form definition for Cuti."""

    class Meta:
        """Meta definition for Cutiform."""

        model = Cuti
        fields = ['jenis_cuti', 'tgl_mulai', 'tgl_selesai', 'alasan', 'sisa_cuti']
        widgets = {
            'tgl_mulai' : DateTimeInput(
                attrs={'type':'datetime-local', 'class':'form-control'}
            ),
            'tgl_selesai' : DateTimeInput(
                attrs={'type':'datetime-local', 'class':'form-control'}
                ),
        }
            
    def __init__(self, *args, **kwargs):
        super(CutiForm, self).__init__(*args, **kwargs)
        self.fields['jenis_cuti'].widget.attrs.update({'id':'jenis_cuti', 'class':'form-control'})
        # self.fields['status'].widget.attrs.update({'id':'status', 'class':'form-control'})
        self.fields['alasan'].widget.attrs.update({'id':'alasan', 'class':'form-control'})
        self.fields['tgl_mulai'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['tgl_selesai'].input_formats = ['%Y-%m-%dT%H:%M']

    def clean(self):
        cleaned_data = super().clean()
        tgl_mulai = cleaned_data.get('tgl_mulai')
        tgl_selesai = cleaned_data.get('tgl_selesai')
        sisa_cuti = cleaned_data.get('sisa_cuti')

        if tgl_mulai and tgl_selesai:
            if tgl_selesai < tgl_mulai:
                raise forms.ValidationError("Tanggal selesai tidak boleh sebelum tanggal mulai")
        
            if tgl_mulai < timezone.now():
                raise forms.ValidationError("Tanggal mulai tidak boleh di masa lalu")
        # return cleaned_data
        try:
            sisa_cuti = int(sisa_cuti)
            if sisa_cuti < 1:
                raise forms.ValidationError("Sisa cuti tidak mencukupi")
        except (ValueError, TypeError):
            raise forms.ValidationError("sisa cuti tidak valid")

        return cleaned_data