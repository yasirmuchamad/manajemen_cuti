from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here
class Cuti(models.Model):
    """Model definition for Cuti."""
    CUTI_CHOICES = [
        ('tahunan', 'Tahunan'),
        ('sakit', 'Sakit'),
        ('darurat', 'Darurat')
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('disetujui', 'Disetujui'),
        ('ditolak', 'Ditolak'),
    ]

    # TODO: Define fields here
    karyawan        = models.ForeignKey(User, on_delete = models.CASCADE)
    jenis_cuti      = models.CharField(
                        max_length = 16,
                        choices = CUTI_CHOICES,
                        default = 'pending'
                        )                        
    tgl_permohonan  = models.DateTimeField(default = timezone.now)
    tgl_mulai       = models.DateTimeField()
    tgl_selesai     = models.DateTimeField()
    status          = models.CharField(
                        max_length = 16,
                        choices = STATUS_CHOICES,
                        default = 'tahunan'
                        )
    alasan          = models.CharField(max_length = 32, blank=True, null=True)
    sisa_cuti       = models.IntegerField()

    class Meta:
        """Meta definition for Cuti."""

        verbose_name = 'Cuti'
        verbose_name_plural = 'Cutis'

    def __str__(self):
        """Unicode representation of Cuti."""
        return f"{self.karyawan}-{self.jenis_cuti}-{self.status}"
