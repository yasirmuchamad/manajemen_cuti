# Generated by Django 5.2.1 on 2025-07-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_cuti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuti',
            name='sisa_cuti',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]
