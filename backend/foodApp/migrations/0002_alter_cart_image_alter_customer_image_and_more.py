# Generated by Django 4.2.7 on 2024-02-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]