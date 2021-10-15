from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import OrderTicketItem


@receiver(post_save, sender=OrderTicketItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update ticket total on ticketitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderTicketItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update OrderTicketItem when the order is deleted
    """
    instance.order.update_total()
