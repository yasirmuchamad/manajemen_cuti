# Generated by Django 5.2.1 on 2025-07-15 10:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_cuti', models.CharField(choices=[('tahunan', 'Tahunan'), ('sakit', 'Sakit'), ('darurat', 'Darurat')], default='pending', max_length=16)),
                ('tgl_permohonan', models.DateTimeField(default=django.utils.timezone.now)),
                ('tgl_mulai', models.DateTimeField()),
                ('tgl_selesai', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('disetujui', 'Disetujui'), ('ditolak', 'Ditolak')], default='tahunan', max_length=16)),
                ('alasan', models.CharField(blank=True, max_length=32, null=True)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cuti',
                'verbose_name_plural': 'Cutis',
            },
        ),
    ]
