# Generated by Django 4.2.1 on 2023-05-13 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]