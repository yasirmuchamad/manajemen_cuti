from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from openpyxl import Workbook
from django.http import HttpResponse


# Create your views here.
@login_required
def listCuti(request):
    # pending_count = Cuti.objects.filter(status='pending').count()
    if request.user.is_staff:
        cuti = Cuti.objects.all().order_by('-tgl_permohonan')
    else:
        cuti = Cuti.objects.filter(karyawan=request.user).order_by('-tgl_permohonan')
    
    context = {
        'title' : "Daftar Permohonan Cuti",
        'cutis' : cuti,
    }
    return render(request, 'manajemen_cuti/list.html', context)

@login_required
def addCuti(request):
    form = CutiForm(request.POST or None)
    if request.method =='POST':
        print("==== DEBUG POST ====")
        for key in request.POST:
            print(f"{key} → {request.POST.getlist(key)}")  # penting: pakai getlist

        if form.is_valid():
            cuti = form.save(commit=False)
            cuti.karyawan = request.user
            cuti.status = 'pending'
            cuti.save()
            print(request.POST)
            print("Tipe alasan:", type(request.POST.get('alasan')))

            return redirect('manajemen_cuti:list_cuti')
        else:
            print("forms error", form.errors)

    context = {
        'title' : 'Permohonan Cuti',
        'forms' : form,
    }

    return render(request, 'manajemen_cuti/create.html', context)

