from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def upate_on_save(sender, instance, created, **kwargs):
    """
    Update order total in lineitem update/create
    """
    instance.order.update_total()


@receiver(post_save, sender=OrderLineItem)
def upate_on_delete(sender, instance, **kwargs):
    """
    Update order total in lineitem delete
    """
    instance.order.update_total()