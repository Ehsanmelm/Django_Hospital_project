# Generated by Django 4.0.6 on 2023-01-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0033_dischargepatientmodel_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
