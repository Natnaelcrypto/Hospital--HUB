# Generated by Django 4.2.3 on 2023-07-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_appointment_created_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_date',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_time',
        ),
    ]
