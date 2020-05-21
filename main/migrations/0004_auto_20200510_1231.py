# Generated by Django 3.0.6 on 2020-05-10 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_checkout_produit'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='confirmer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkout',
            name='prix',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='produit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Produit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkout',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
