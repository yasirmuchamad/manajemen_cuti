from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Cuti)
class CutiAdmin(admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_cuti', 'tgl_permohonan', 'tgl_mulai', 'tgl_selesai', 'status', 'alasan']