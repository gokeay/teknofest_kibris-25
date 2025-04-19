# Generated by Django 4.2.7 on 2025-03-16 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='T3PersonelVeriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koordinatorluk', models.CharField(max_length=100)),
                ('birim', models.CharField(max_length=100)),
                ('ogle_yemegi', models.PositiveIntegerField()),
                ('aksam_yemegi', models.PositiveIntegerField()),
                ('lunchbox', models.PositiveIntegerField(default=0)),
                ('submitteddate', models.DateField(auto_now_add=True)),
                ('submittedtime', models.TimeField(auto_now_add=True)),
                ('kisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t3_veriler', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'T3 Personel Verisi',
                'verbose_name_plural': 'T3 Personel Verileri',
                'db_table': 't3personel_veriler',
            },
        ),
        migrations.CreateModel(
            name='SorumluVeriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gun', models.DateField()),
                ('personel_yemek_siparis', models.PositiveIntegerField()),
                ('taseron_yemek_siparis', models.PositiveIntegerField()),
                ('submitteddate', models.DateField(auto_now_add=True)),
                ('submittedtime', models.TimeField(auto_now_add=True)),
                ('kisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorumlu_veriler', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sorumlu Verisi',
                'verbose_name_plural': 'Sorumlu Verileri',
                'db_table': 'sorumlu_veriler',
            },
        ),
        migrations.CreateModel(
            name='GonulluSorunVeriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gun', models.DateField()),
                ('saat', models.TimeField()),
                ('alan', models.CharField(max_length=100)),
                ('aciklama', models.TextField()),
                ('fotograf', models.ImageField(blank=True, null=True, upload_to='gonullu_sorun_fotolar/')),
                ('submitteddate', models.DateField(auto_now_add=True)),
                ('submittedtime', models.TimeField(auto_now_add=True)),
                ('kisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gonullu_sorun_veriler', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gönüllü Sorun Verisi',
                'verbose_name_plural': 'Gönüllü Sorun Verileri',
                'db_table': 'gonullu_sorun_veriler',
            },
        ),
        migrations.CreateModel(
            name='GonulluDurumVeriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gun', models.DateField()),
                ('saat', models.TimeField()),
                ('alan', models.CharField(max_length=100)),
                ('aciklama', models.TextField()),
                ('fotograf', models.ImageField(blank=True, null=True, upload_to='gonullu_durum_fotolar/')),
                ('submitteddate', models.DateField(auto_now_add=True)),
                ('submittedtime', models.TimeField(auto_now_add=True)),
                ('kisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gonullu_durum_veriler', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gönüllü Durum Verisi',
                'verbose_name_plural': 'Gönüllü Durum Verileri',
                'db_table': 'gonullu_durum_veriler',
            },
        ),
        migrations.CreateModel(
            name='T3PersonelAtama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koordinatorluk', models.CharField(max_length=100)),
                ('birim', models.CharField(max_length=100)),
                ('kisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atamalar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'T3 Personel Ataması',
                'verbose_name_plural': 'T3 Personel Atamaları',
                'db_table': 't3personel_atama',
                'unique_together': {('kisi', 'koordinatorluk', 'birim')},
            },
        ),
    ]
