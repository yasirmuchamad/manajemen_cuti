from django.test import TestCase
from django.contrib.auth.models import User
from manajemen_cuti.models import Cuti
from django.utils import timezone
from datetime import timedelta

class CutiModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='yassir', password='123')

    def test_str_representation(self):
        cuti = Cuti.objects.create(
            karyawan = self.user,
            jenis_cuti="tahunan", 
            tgl_mulai=timezone.now()+timedelta(days=1), 
            tgl_selesai=timezone.now()+timedelta(days=2), 
            tgl_permohonan=timezone.now(),
            status='pending', 
            alasan='interview',
            sisa_cuti=4
            )
        self.assertEqual(str(cuti), 'yassir-tahunan-pending')

    def test_default_status(self):
        cuti = Cuti.objects.create(
            karyawan = self.user,
            jenis_cuti="tahunan", 
            tgl_mulai=timezone.now()+timedelta(days=1), 
            tgl_selesai=timezone.now()+timedelta(days=2), 
            tgl_permohonan=timezone.now(),
            alasan='interview',
            sisa_cuti=4
            )
        self.assertEqual(cuti.status, 'pending')
    
    def test_foreign_key_karyawan(self):
        cuti = Cuti.objects.create(
            karyawan = self.user,
            jenis_cuti="tahunan", 
            tgl_mulai=timezone.now()+timedelta(days=1), 
            tgl_selesai=timezone.now()+timedelta(days=2), 
            tgl_permohonan=timezone.now(),
            alasan='interview',
            sisa_cuti=4
            )
        self.assertEqual(cuti.karyawan.username, 'yassir')

    def test_signal_sisa_cuti_berkurang(self):
        cuti = Cuti.objects.create(
            karyawan = self.user,
            jenis_cuti="tahunan", 
            tgl_mulai=timezone.now()+timedelta(days=1), 
            tgl_selesai=timezone.now()+timedelta(days=2), 
            tgl_permohonan=timezone.now(),
            alasan='interview',
            sisa_cuti=4
            )

        # ubah.status menjadi disetujui
        cuti.status = 'disetujui'
        cuti.save()

        # Ambil ulang dari DB (Karena instance lama bisa stale)
        update_cuti = Cuti.objects.get(id=cuti.id)
        self.assertEqual(update_cuti.sisa_cuti, 3)

    def test_filter_by_karyawan(self):
        self.user2 = User.objects.create(username='user2', password='456')

        #buat dua cuti, masing untuk user
        Cuti.objects.create(
            karyawan = self.user,
            jenis_cuti="tahunan", 
            tgl_mulai=timezone.now()+timedelta(days=1), 
            tgl_selesai=timezone.now()+timedelta(days=2), 
            tgl_permohonan=timezone.now(),
            alasan='interview',
            sisa_cuti=4
            )
        Cuti.objects.create(
            karyawan = self.user2,
            jenis_cuti="tahunan", 
            tgl_mulai=timezone.now()+timedelta(days=1), 
            tgl_selesai=timezone.now()+timedelta(days=2), 
            tgl_permohonan=timezone.now(),
            alasan='jalan jalan',
            sisa_cuti=5
            )

        result = Cuti.objects.filter(karyawan=self.user)
        self.assertEqual(result.count(), 1)
        self.assertEqual(result[0].karyawan.username, 'yassir')
        