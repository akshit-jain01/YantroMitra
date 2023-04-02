import random, time
from django.core.mail import send_mail
from django.conf import settings

from .models import OTP

def send_otp_email(email):

    OTP.objects.filter(otp_email__iexact = email).delete()
    subject = "Your Account verification email"
    otp = random.randint(1000,9999)
    message = f'your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])

    time_created = int(time.time())

    otp_obj = OTP.objects.create(otp=otp, otp_email = email, time_created = time_created)
    otp_obj.save()