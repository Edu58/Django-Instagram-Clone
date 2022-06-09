# Generated by Django 4.0.5 on 2022-06-07 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.image'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.profile'),
        ),
    ]