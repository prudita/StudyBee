# Generated by Django 4.1.7 on 2023-03-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_bee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionrecord',
            name='type',
            field=models.CharField(choices=[('Pengeluaran', 'Pengeluaran'), ('Pemasukan', 'Pemasukan')], max_length=20),
        ),
    ]
