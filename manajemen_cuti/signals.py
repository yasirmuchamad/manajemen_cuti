from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Cuti

@receiver(pre_save, sender=Cuti)
def check_status_change(sender, instance, **kwargs):
    try:
        old = Cuti.objects.get(pk=instance.pk)
    except Cuti.DoesNotExist:
        return #return nilai kosong

    if old.status != instance.status:
        if instance.status == 'disetujui' and instance.sisa_cuti>0:
            instance.sisa_cuti -= 1
        elif instance.status == 'dibatalkan':
            instance.sisa_cuti += 1

