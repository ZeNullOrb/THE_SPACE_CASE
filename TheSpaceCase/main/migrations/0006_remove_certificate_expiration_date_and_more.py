# Generated by Django 4.1.6 on 2023-02-27 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='issue_date',
        ),
    ]
