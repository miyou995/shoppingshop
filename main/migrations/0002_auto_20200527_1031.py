# Generated by Django 3.0.6 on 2020-05-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkout',
            options={'ordering': ['wilaya']},
        ),
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/produits'),
        ),
    ]
