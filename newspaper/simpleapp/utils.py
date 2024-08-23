# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from .models import PostCategory
# from django.conf import settings
#
#
# def send_notifications(preview, pk, title, subscribers):
#     html_content = render_to_string(
#         'email/post_send_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}',
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
