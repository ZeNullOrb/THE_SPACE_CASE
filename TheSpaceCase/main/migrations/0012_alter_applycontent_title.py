# Generated by Django 4.1.5 on 2023-03-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_applycontent_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applycontent',
            name='title',
            field=models.CharField(max_length=512),
        ),
    ]
