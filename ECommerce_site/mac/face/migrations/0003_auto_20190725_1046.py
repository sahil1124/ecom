# Generated by Django 2.2.2 on 2019-07-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_auto_20190717_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='shop/images'),
        ),
    ]