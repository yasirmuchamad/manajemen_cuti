from django.test import TestCase, Client
from django.contrib.auth.models import User
from manajemen_cuti.models import Cuti
from django.urls import reverse
from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import timedelta, datetime

# Create your tests here.
class CutiViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='123')
        self.user2 = User.objects.create_user(username='user2', password='123')
        now = timezone.now()

        Cuti.objects.create(
            karyawan=self.user1,
            jenis_cuti='tahunan',
            tgl_mulai=now,
            tgl_selesai=now+timedelta(days=2),
            tgl_permohonan=now,
            status='pending',
            alasan='alasan user1',
            sisa_cuti=5,
        )

        Cuti.objects.create(
            karyawan=self.user2,
            jenis_cuti='tahunan',
            tgl_mulai=now,
            tgl_selesai=now+timedelta(days=2),
            tgl_permohonan=now,
            status='pending',
            alasan='alasan user2',
            sisa_cuti=5,
        )

        
    def test_user1_hanya_lihat_cutinya_sendiri(self):
        self.client.login(username='user1', password='123')
        response = self.client.get(reverse('manajemen_cuti:list_cuti'))

        self.assertContains(response, 'alasan user1')

        self.assertNotContains(response, 'alasan user2')

    