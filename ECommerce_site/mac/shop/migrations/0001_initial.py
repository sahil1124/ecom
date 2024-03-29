# Generated by Django 2.2.2 on 2019-07-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default=' ', max_length=50)),
                ('phone', models.IntegerField(default=' ')),
                ('desc', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=500)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.IntegerField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default=' ', max_length=50)),
                ('subcategory', models.CharField(default=' ', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=3000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default=' ', upload_to='shop/images')),
            ],
        ),
    ]
