# Generated by Django 4.0.6 on 2022-11-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]