# Generated by Django 4.2 on 2023-07-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monespace', '0006_dmdcredit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dmdcredit',
            name='idclt',
        ),
        migrations.AddField(
            model_name='dmdcredit',
            name='nomclt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dmdcredit',
            name='noment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
