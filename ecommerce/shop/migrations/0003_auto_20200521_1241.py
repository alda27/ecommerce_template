# Generated by Django 3.0.4 on 2020-05-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productcollection_presentation_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcollection',
            name='view_name',
            field=models.CharField(default='sweats', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='clothe_size',
            field=models.ManyToManyField(blank=True, to='shop.ClotheSize'),
        ),
    ]