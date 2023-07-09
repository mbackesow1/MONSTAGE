# Generated by Django 4.2 on 2023-07-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monespace', '0005_alter_entreprise_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='DmdCredit',
            fields=[
                ('iddmd', models.AutoField(primary_key=True, serialize=False)),
                ('idclt', models.IntegerField()),
                ('noment', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('idpro', models.IntegerField()),
            ],
            options={
                'db_table': 'dmdcredit',
            },
        ),
    ]