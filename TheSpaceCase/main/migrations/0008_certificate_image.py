# Generated by Django 4.1.6 on 2023-02-27 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_company_image_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(default='images/certificate.jpg', upload_to='images/'),
        ),
    ]
