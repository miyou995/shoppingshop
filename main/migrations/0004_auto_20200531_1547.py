# Generated by Django 3.0.6 on 2020-05-31 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200531_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cout_livraison',
            field=models.CharField(choices=[('AL', 400), ('AU', 600)], default='AU', max_length=2),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='montant_total',
            field=models.IntegerField(default=0),
        ),
    ]
