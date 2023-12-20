from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from onlineStore.celery import app


# @app.task(bind=True)
@shared_task
def delivery(review_text, user_email):
    # Query the Order Model for the to obtain the Order object.
    # order = Order.objects.get(id=order_id)
    # subject = f'Order nr. {order.id}'
    # message = f'Dear {order.first_name},\n\nYou have successfully placed an order. Your order ID is {order.id}.'
    # mail_sent = send_mail(
    #     subject=subject,
    #     message=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[order.email]
    # )
    # user_email = 'request.user.email'  # Предположим, что пользователь аутентифицирован
    # review_text = form.cleaned_data['review_text'] + " -- FROM --\n" + user_email
    send_mail('Отзыв', review_text, user_email, ['matveenkoalena2844@gmail.com'])
    # mail_sent ='Отзыв' + review_text + user_email+'matveenkoalena2844@gmail.com'
    # print(mail_sent)

