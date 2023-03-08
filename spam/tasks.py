from celery import shared_task
from django.core.mail import send_mail
from spam.models import Contact

@shared_task
def send_spam():
    emails = [i.email for i in Contact.objects.all()]
    send_mail(
        'Py25 shop project', # title
        f'привет загляни на наш сайт', # body
        'kalykulovbekzan@gmail.com', # from
        emails # to
    )
