# Generated by Django 4.0 on 2022-01-08 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_seller_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to='Profile'),
        ),
    ]