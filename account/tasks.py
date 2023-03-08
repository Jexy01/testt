from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, code):
    import time
    time.sleep()
    send_mail(
        'Py25 shop project', # title
        f'http://localhost:8000/api/v1/account/activate/{code}', # body
        'kalykulovbekzan@gmail.com', # from
        [email] # to
    )