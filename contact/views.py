from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.conf import settings

# Create your views here.


def contact(request):
    """Render contact page and send confirmation email"""
    full_name = None
    email = None
    subject = None
    message = None

    if request.method == "POST":
        enquire = request.POST['message']
        email = request.POST['email']
        full_name = request.POST['full_name']
        subject = request.POST['subject']

        # Send an email to site owner
        current_site = get_current_site(request)
        mail_subject = subject
        message = render_to_string(
            'emails/enquire.html', {
                'enquire': enquire,
                'email': email,
                'full_name': full_name,
                'domain': current_site,
            })
        to_email = settings.EMAIL_HOST_USER
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()

        # Send a confirmation email to the user
        current_site = get_current_site(request)
        mail_subject = subject
        message = render_to_string(
            'emails/confirmation_email.html', {
                'domain': current_site,
                'enquire': enquire,
                'email': email,
                'full_name': full_name,
            })
        to_email = email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        messages.success(request, f"Thank you {full_name} for your message,"
                         "Somebody from our team will get in touch shortly")
        return redirect('home')

    context = {
        'full_name': full_name,
        'email': email,
        'subject': subject,
        'message': message,
    }

    return render(request, 'contact/contact.html', context)


def about(request):
    """Render the view for About Page"""
    return render(request, 'about/about.html')
