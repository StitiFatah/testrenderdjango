# Generated by Django 4.0 on 2022-01-13 19:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersoUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email Adress')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=200, verbose_name='firstname')),
                ('last_name', models.CharField(max_length=200, verbose_name='lastname')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]