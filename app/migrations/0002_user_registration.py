# Generated by Django 4.2.1 on 2024-05-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registration',
            field=models.DateField(auto_now=True),
        ),
    ]
