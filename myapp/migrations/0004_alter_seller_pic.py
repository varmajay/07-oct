# Generated by Django 4.0 on 2022-01-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_seller_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='pic',
            field=models.FileField(default='avtar.png', upload_to='Profile'),
        ),
    ]