from django.test import TestCase
from manajemen_cuti.forms import *
from datetime import date, timedelta

class CutiFormTest(TestCase):
    def test_valid_form(self):
        form = CutiForm(data={
            'jenis_cuti':'tahunan',
            'tgl_mulai':date.today()+timedelta(days=1),
            'tgl_selesai':date.today()+timedelta(days=3),
            'alasan':'liburan keluarga'
        })
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
            'alasan':'terlambat pengajuan'
        })

        self.assertFalse(form.is_valid())
        self.assertIn("Tanggal mulai tidak boleh di masa lalu", str(form.errors))