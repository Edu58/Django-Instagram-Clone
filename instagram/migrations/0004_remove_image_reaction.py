# Generated by Django 4.0.5 on 2022-06-07 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_alter_likes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='reaction',
        ),
    ]
