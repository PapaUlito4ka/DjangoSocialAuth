# Generated by Django 3.2.9 on 2021-11-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
