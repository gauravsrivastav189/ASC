# Generated by Django 4.1.3 on 2023-11-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_taskinfo_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinfo',
            name='notification_created_label',
            field=models.CharField(default='Notification Not Sent', max_length=255),
        ),
    ]