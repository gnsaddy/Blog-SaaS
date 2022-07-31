# Generated by Django 4.0.5 on 2022-07-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0006_alter_facultyusermodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]