# Generated by Django 4.0.6 on 2022-12-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0032_alter_patientmodel_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='dischargepatientmodel',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
