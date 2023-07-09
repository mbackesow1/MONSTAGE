# Generated by Django 4.2 on 2023-07-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idpro', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'orbitproduct',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('idu', models.BigAutoField(primary_key=True, serialize=False)),
                ('nompreu', models.CharField(max_length=100, null=True)),
                ('emailu', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email')),
                ('teleu', models.CharField(max_length=15, null=True, verbose_name='Télephoene')),
                ('mdpu', models.CharField(max_length=128, null=True, verbose_name='Mode de Passse')),
                ('entreprise', models.CharField(choices=[('ccbm', 'ccbm'), ('orbit', 'orbit')], max_length=30, verbose_name='Entreprise')),
                ('postu', models.CharField(max_length=128, null=True, verbose_name='Pste')),
                ('sectu', models.CharField(max_length=128, null=True, verbose_name='Secteur')),
                ('adresseu', models.CharField(max_length=15, null=True, verbose_name='Adresse')),
                ('dateinsu', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date creation')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Profol')),
            ],
            options={
                'db_table': 'orbituser',
            },
        ),
    ]
