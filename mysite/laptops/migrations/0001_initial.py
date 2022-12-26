# Generated by Django 4.0.1 on 2022-10-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('Marka', models.CharField(db_column='Marka', max_length=30)),
                ('Model', models.CharField(db_column='Model', max_length=100)),
                ('Isletim_Sistemi', models.CharField(db_column='Isletim Sistemi', max_length=100)),
                ('Islemci', models.CharField(db_column='Islemci', max_length=100)),
                ('Bellek', models.CharField(db_column='Bellek', max_length=30)),
                ('Disk', models.CharField(db_column='Disk', max_length=50)),
                ('Ekran_Boyutu', models.CharField(db_column='Ekran Boyutu', max_length=20)),
                ('Puan', models.CharField(db_column='Puan', max_length=3)),
                ('Fiyat', models.CharField(db_column='Fiyat', max_length=7)),
                ('Baslik', models.CharField(db_column='Baslik', max_length=255)),
                ('Resim', models.CharField(db_column='Foto', max_length=255)),
                ('Site', models.CharField(db_column='Site', max_length=12)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]