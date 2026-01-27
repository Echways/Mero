from django.conf import settings
from django.core.mail import EmailMessage


def send_ticket_email(registration):
    event = registration.event
    subject = f"Ваш билет на {event.title}"
    body = (
        f"Здравствуйте, {registration.first_name}!\n\n"
        f"Вы зарегистрированы на событие: {event.title}.\n"
        f"Тип билета: {registration.get_ticket_type_display()}.\n\n"
        "Спасибо за регистрацию!"
    )
    email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [registration.email])

    if event.ticket_image and event.ticket_image.name:
        email.attach_file(event.ticket_image.path)

    email.send(fail_silently=False)
