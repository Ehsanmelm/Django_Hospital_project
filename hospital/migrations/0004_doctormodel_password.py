# Generated by Django 4.0.6 on 2022-10-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_remove_patientmodel_admitdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctormodel',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
    ]
