# Generated by Django 4.0.6 on 2022-11-19 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_rename_appointment_appointmentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentmodel',
            old_name='patinet_pass',
            new_name='patient_pass',
        ),
    ]