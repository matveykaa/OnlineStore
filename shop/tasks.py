from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from onlineStore.celery import app


@shared_task
def delivery(review_text, user_email):
    send_mail('Отзыв', review_text, user_email, ['matveenkoalena2844@gmail.com'])


