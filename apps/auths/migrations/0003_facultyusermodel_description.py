# Generated by Django 4.0.5 on 2022-07-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_customuser_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyusermodel',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
