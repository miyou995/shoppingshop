# Generated by Django 3.0.6 on 2020-05-10 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200510_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='produit',
        ),
    ]
