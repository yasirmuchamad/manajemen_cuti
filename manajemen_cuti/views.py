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
            cuti.sisa_cuti = 6
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

@user_passes_test(lambda u:u.is_staff)
def approveCuti(request, pk):
    cuti = Cuti.objects.get(pk=pk)
    cuti.status = 'disetujui'
    cuti.save()

    return redirect('manajemen_cuti:list_cuti')

@user_passes_test(lambda u:u.is_staff)
def cancelCuti(request, pk):
    cuti = Cuti.objects.get(pk=pk)
    cuti.status = 'dibatalkan'
    cuti.save()

    return redirect('manajemen_cuti:list_cuti')

@user_passes_test(lambda u:u.is_staff)
def rejectCuti(request, pk):
    cuti = Cuti.objects.get(pk=pk)
    cuti.status = 'ditolak'
    cuti.save()

    return redirect('manajemen_cuti:list_cuti')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('manajemen_cuti:list_cuti')
            else:
                # messages.error(request, 'Username atau password salah.')
                context = {
                    'forms': form,
                    'error': 'Invalid Username or Password',
                    'title': 'Login',
                    'subtitle': 'Form',
                }
                # messages.success(request, f'Selamat Datang , {user.username}')
                return render(request, 'manajemen_cuti/login.html', context)
        else:
            # print("Form errors:", form.errors)
            # messages.error(request, 'Username atau Password anda salah.')
            # messages.error(request, 'Form tidak valid. Coba lagi.')
            context = {
                'forms': form,
                'error': 'Invalid Username or Password',
                'title': 'Login',
                'subtitle': 'Form',
            }
            return render(request, 'manajemen_cuti/login.html', context)
    
    # Get request
    form = AuthenticationForm()
    context = {
        'title' : 'Login Form',
        'forms' : form,
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('manajemen_cuti:login')