"# Generated by Django 4.2.7 on 2025-03-16 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('tc', models.CharField(max_length=11, unique=True)),
                ('tel_no', models.CharField(blank=True, max_length=15, null=True)),
                ('isim', models.CharField(max_length=50)),
                ('soyisim', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('gonullu', 'Gönüllü'), ('t3personel', 'T3 Personel'), ('sorumlu', 'Sorumlu'), ('izleyici', 'İzleyici'), ('admin', 'Admin')], default='gonullu', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('submitteddate', models.DateField(auto_now_add=True)),
                ('submittedtime', models.TimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'verbose_name_plural': 'Kullanıcılar',
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('islem', models.CharField(max_length=255)),
                ('sayfa', models.CharField(max_length=255)),
                ('tarih', models.DateField(auto_now_add=True)),
                ('saat', models.TimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('tarayici_bilgisi', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kullanıcı Logu',
                'verbose_name_plural': 'Kullanıcı Logları',
                'db_table': 'logs',
            },
        ),
    ]
