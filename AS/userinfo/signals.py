from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from userinfo.models import TaskInfo

@receiver(post_save, sender=TaskInfo)
def task_assigned_notification(sender, instance, created, **kwargs):
    if created and instance.status == 'assigned':
        notify(sender=instance.created_by, recipient=instance.assigned_to, verb='New task assigned to you.', description=f'You have a new task to complete. Please visit the task list to view the task details.')
