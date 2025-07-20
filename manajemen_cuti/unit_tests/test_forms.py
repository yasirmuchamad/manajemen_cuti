from django.test import TestCase
from manajemen_cuti.forms import *
from datetime import date, timedelta

class CutiFormTest(TestCase):
    def test_valid_form(self):
        form = CutiForm(data={
            'jenis_cuti':'tahunan',
            'tgl_mulai':date.today()+timedelta(days=1),
            'tgl_selesai':date.today()+timedelta(days=3),
            'alasan':'liburan keluarga',
            'sisa_cuti':2
        })
        # form.instance.karywan = user
        self.assertTrue(form.is_valid())

    def test_tgl_selesai_lebih_awal(self):
        form = CutiForm(data={
            'jenis_cuti':'tahunan',
            'tgl_mulai':date.today()+timedelta(days=3),
            'tgl_selesai':date.today()+timedelta(days=1),
            'alasan':'error date'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Tanggal selesai tidak boleh sebelum tanggal mulai', str(form.errors))

    def test_tgl_mulai_di_masa_lalu(self):
        form = CutiForm(data={
            'jenis_cuti':'tahunan',
            'tgl_mulai':date.today()-timedelta(days=3),
            'tgl_selesai':date.today()-timedelta(days=2),
            'alasan':'terlambat pengajuan',
            'sisa_cuti':5
        })

        self.assertFalse(form.is_valid())
        self.assertIn("Tanggal mulai tidak boleh di masa lalu", str(form.errors))

    def test_sisa_cuti_kurang_dari_satu(self):
        user = User.objects.create_user(username='testuser', password='123')

        form_data = {
            'jenis_cuti': 'tahunan',
            'tgl_mulai': timezone.now()+timedelta(days=1),
            'tgl_selesai': timezone.now()+timedelta(days=2),
            'alasan': 'liburan',
            'sisa_cuti':0
        }

        form=CutiForm(data=form_data)
        form.instance.karywan = user
        self.assertFalse(form.is_valid())
        self.assertIn("sisa cuti tidak mencukupi", str(form.errors).lower())