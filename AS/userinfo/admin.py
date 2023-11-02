# from django.contrib import admin
# from notifications.signals import notify
# from userinfo.models import TaskInfo

# class TaskInfoAdmin(admin.ModelAdmin):
#     actions = ['assign_task', 'send_notification']
#     list_display = ('name', 'assigned_to', 'status', 'notification_status', 'notification_created_label')

#     def assign_task(self, request, queryset):
#         for task in queryset:
#             task.status = 'assigned'
#             task.save()

#             # Update the notification created label.
#             task.notification_created_label = 'Notification Created'
#             task.save()

#             notify(sender=request.user, recipient=task.assigned_to, verb='New task assigned to you.', description=f'You have a new task to complete: {task.name}. Please visit the task list to view the task details.')

#     def send_notification(self, request, queryset):
#         for task in queryset:
#             task.notification_status = 'sent'
#             task.save()

#             # Update the notification created label.
#             task.notification_created_label = 'Notification Sent'
#             task.save()

#             notify(sender=request.user, recipient=task.assigned_to, verb='New task assigned to you.', description=f'You have a new task to complete: {task.name}. Please visit the task list to view the task details.')


# from django.contrib import admin
# from userinfo.models import TaskInfo
# from userinfo.admin import TaskInfoAdmin

# admin.site.register(TaskInfo, TaskInfoAdmin)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from notifications.models import Notification

# class CustomUserAdmin(UserAdmin):
#     list_display = UserAdmin.list_display + ('user_notifications',)

#     def user_notifications(self, obj):
#         notifications = Notification.objects.filter(recipient=obj)
#         return ", ".join([notification.verb for notification in notifications])

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)


from django.contrib import admin
from notifications.signals import notify
from userinfo.models import TaskInfo
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from notifications.models import Notification
from django.urls import reverse
from django.utils.html import format_html

class TaskInfoAdmin(admin.ModelAdmin):
    actions = ['assign_task', 'send_notification']
    list_display = ('name', 'assigned_to', 'status', 'notification_status', 'notification_created_label')

    def assign_task(self, request, queryset):
        for task in queryset:
            task.status = 'assigned'
            task.save()

            # Update the notification created label.
            task.notification_created_label = 'Notification Created'
            task.save()

            notify(sender=request.user, recipient=task.assigned_to, verb='New task assigned to you.', description=f'You have a new task to complete: {task.name}. Please visit the task list to view the task details.')

    def send_notification(self, request, queryset):
        for task in queryset:
            task.notification_status = 'sent'
            task.save()

            # Update the notification created label.
            task.notification_created_label = 'Notification Sent'
            task.save()

            notify(sender=request.user, recipient=task.assigned_to, verb='New task assigned to you.', description=f'You have a new task to complete: {task.name}. Please visit the task list to view the task details.')

admin.site.register(TaskInfo, TaskInfoAdmin)

# class CustomUserAdmin(UserAdmin):
#     list_display = UserAdmin.list_display + ('user_notifications',)

#     def user_notifications(self, obj):
#         notifications = Notification.objects.filter(recipient=obj)
#         notifications_info = [
#             format_html('<a href="{}">{}</a>'.format(
#                 reverse("admin:notifications_notification_change", args=(notification.id,)),
#                 notification.verb)
#             )
#             for notification in notifications
#         ]
#         return format_html("".join(notifications_info))

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from notifications.models import Notification
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_notifications')

    def user_notifications(self, obj):
        notifications = Notification.objects.filter(recipient=obj)
        notifications_info = [
            format_html('<a href="{}">{}</a>'.format(
                reverse("admin:notifications_notification_change", args=(notification.id,)),
                notification.verb)
            )
            for notification in notifications
        ]
        return format_html(", ".join(notifications_info))

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
