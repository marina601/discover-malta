# pylint: disable=no-member
import json
import time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from trips.models import Trip
from .models import Order, OrderTicketItem
from accounts.models import UserProfile


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request
    
    def _send_confirmation_email(self, order):

        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'Your order confirmation',
            {'order': order})
        body = render_to_string('checkout/emails/confirmation_email.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
         )

    def handle_event(self, event):
        """
        Handle generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        bag_dict = json.loads(bag)
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the billing address details
        for field, value in billing_details.address.items():
            if value == " ":
                billing_details.address[field] = None
        
        # Update profile information if the save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.username_phone_number = billing_details.phone
                profile.country = billing_details.address.country
                profile.postcode = billing_details.address.postal_code
                profile.town_or_city = billing_details.address.city
                profile.street_address1 = billing_details.address.line1
                profile.street_address2 = billing_details.address.line2
                profile.county = billing_details.address.state
                profile.save()
     
        # If does not exist, get all the details from the form
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                        first_name__iexact=billing_details.name.split(' ')[0],
                        last_name__iexact=billing_details.name.split(' ')[-1],
                        user_profile=profile,
                        email__iexact=billing_details.email,
                        phone_number__iexact=billing_details.phone,
                        country__iexact=billing_details.address.country,
                        postcode__iexact=billing_details.address.postal_code,
                        town_or_city__iexact=billing_details.address.city,
                        street_address1__iexact=billing_details.address.line1,
                        street_address2__iexact=billing_details.address.line2,
                        county__iexact=billing_details.address.state,
                        grand_total=grand_total,
                        original_bag=bag_dict,
                        stripe_pid=pid,
                    )
                # If order exist send a response to Stripe
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Success:'
                        f' Verified order already in the database',
                status=200)
        else:
            # If order does not exists get all the values from the form
            # Iterate through bag items
            # Create an order in the database
            order = None
            try:
                order = Order.objects.create(
                    first_name=billing_details.name.split(' ')[0],
                    last_name=billing_details.name.split(" ")[1],
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag_dict,
                    stripe_pid=pid,
                )
                for key, values in bag_dict.items():
                    trip = get_object_or_404(Trip, pk=key)
                    order_ticket_item = OrderTicketItem(
                        order=order,
                        trip=trip,
                        child_quantity=bag_dict[key]['children_tickets'],
                        adult_quantity=bag_dict[key]['adult_tickets'],
                        booking_date=bag_dict[key]['booking_date'],
                        quantity=bag_dict[key]['quantity'],
                    )
                    order_ticket_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
