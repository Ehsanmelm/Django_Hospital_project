# Generated by Django 4.0.6 on 2022-10-21 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_patientmodel_assigneddoctorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientmodel',
            name='admitDate',
        ),
    ]
