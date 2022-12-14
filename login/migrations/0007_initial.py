# Generated by Django 4.0.5 on 2022-12-20 04:01

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login', '0006_remove_detailuser_user_ptr_delete_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailUser',
            fields=[
                ('relate_user_id', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_user', models.BooleanField(default=True, verbose_name='Is User')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
