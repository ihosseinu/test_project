# Generated by Django 4.0.1 on 2022-01-30 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(help_text='Phone number should be like this format: 09135556677', max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number.', regex='\\d{11}')], verbose_name='Phone'),
        ),
    ]
