# !!!!!!Работа с классическим сигналом!!!!!
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
#
#
# from .models import PostCategory
# from .utils import send_notifications
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = cat.subscribers.all()
#             subscribers_emails += [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)
#
#
#

# Работа через celery+redis!!!!!
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory
from .tasks import send_email_task


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        send_email_task.delay(instance.pk)
