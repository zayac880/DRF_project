# Generated by Django 4.2.6 on 2023-10-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_user_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='телеграмм id'),
        ),
    ]
