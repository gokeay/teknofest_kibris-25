# Generated by Django 5.1.6 on 2025-04-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20250412_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemAyarlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anahtar', models.CharField(max_length=50, unique=True)),
                ('deger', models.CharField(max_length=255)),
                ('aciklama', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Sistem Ayarı',
                'verbose_name_plural': 'Sistem Ayarları',
            },
        ),
        migrations.AddField(
            model_name='t3personelveriler',
            name='coffee_break',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
