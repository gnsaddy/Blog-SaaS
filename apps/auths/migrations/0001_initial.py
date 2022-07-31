# Generated by Django 4.0.5 on 2022-07-20 18:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('sid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('mobile', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message='Mobile number must be a number.', regex='^[0-9]*$')], verbose_name='mobile number')),
                ('admin', models.BooleanField(default=False, null=True)),
                ('faculty', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('support', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacultyUserModel',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.CharField(max_length=100, null=True, verbose_name='Designation')),
                ('expertise', models.CharField(max_length=100, null=True, verbose_name='Expertise')),
                ('experience', models.CharField(max_length=100, null=True, verbose_name='Experience')),
            ],
            options={
                'db_table': 'faculty_user',
            },
            bases=('auths.customuser',),
        ),
    ]
