from django.db import models
from django.contrib.auth.models import User
from notifications.models import Notification

class TaskInfo(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=255, choices=[('new', 'New'), ('assigned', 'Assigned'), ('completed', 'Completed')])
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    notifications = models.ManyToManyField(Notification, blank=True)
    notification_status = models.CharField(max_length=255, choices=[('pending', 'Pending'), ('sent', 'Sent')], default='pending')
    notification_created_label = models.CharField(max_length=255, default='Notification Not Sent')

    def __str__(self):
        return self.name

