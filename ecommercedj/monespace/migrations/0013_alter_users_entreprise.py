# Generated by Django 4.2 on 2023-07-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monespace', '0012_alter_users_adresseu_alter_users_emailu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='entreprise',
            field=models.CharField(choices=[('ccbm', 'ccbm'), ('orbit', 'orbit')], max_length=30),
        ),
    ]