from django.contrib import admin
from .models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('trip', 'available_days',
                    'tickets_available', 'provider')

admin.site.register(Ticket, TicketAdmin)