# Generated by Django 4.0 on 2022-02-05 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_remove_cart_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]