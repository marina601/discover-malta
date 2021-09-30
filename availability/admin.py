from django.contrib import admin
from . models import Ticket


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('trip', 'booking_date', 'total_num_tickets', 'total_price')


admin.site.register(Ticket, TicketAdmin)
