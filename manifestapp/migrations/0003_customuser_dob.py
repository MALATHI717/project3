# Generated by Django 5.1.7 on 2025-03-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manifestapp', '0002_remove_userprofile_phone_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
