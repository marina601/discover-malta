from django.contrib import admin
from .models import Order, OrderTicketItem


class OrderTicketItemAdminInline(admin.TabularInline):
    """
    Order Ticket Item is available to edit in the
    admin portal
    """
    model = OrderTicketItem
    readonly_fields = ('adult_tickets', 'children_tickets',
                       'ticketitem_total', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    """
    Order is available to view and edit in the
    admin dashboard
    """
    inlines = (OrderTicketItemAdminInline,)

    readonly_fields = ('order_number', 'user_profile', 'date',
                       'order_total', 'grand_total',
                       'original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'first_name',
              'last_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'order_total', 'grand_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
