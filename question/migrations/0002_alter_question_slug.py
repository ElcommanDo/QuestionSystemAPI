# Generated by Django 3.2.6 on 2021-11-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]