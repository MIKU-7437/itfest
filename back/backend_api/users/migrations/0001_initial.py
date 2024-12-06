# Generated by Django 4.2.5 on 2023-11-16 17:32

from django.db import migrations, models
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
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Почта')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('region', models.CharField(max_length=50, verbose_name='Область')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Телефон')),
                ('photo', models.ImageField(blank=True, default='customer_photos/default-profile-picture.jpg', null=True, upload_to='customer_photos/', verbose_name='Фото')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_custom', to='auth.group', verbose_name='Группы')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_custom', to='auth.permission', verbose_name='Права пользователя')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]