# Generated by Django 3.2.13 on 2022-11-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20221104_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='secession',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
