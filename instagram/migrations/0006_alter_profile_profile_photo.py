# Generated by Django 4.0.5 on 2022-06-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
