# Generated by Django 5.0 on 2024-01-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photocard',
            name='description',
        ),
        migrations.AddField(
            model_name='photocard',
            name='delivery_cost',
            field=models.CharField(default='Default Delivery Cost', max_length=200),
        ),
        migrations.AddField(
            model_name='photocard',
            name='delivery_time',
            field=models.TextField(default='Default Delivery Time'),
        ),
        migrations.AddField(
            model_name='photocard',
            name='name',
            field=models.TextField(default='Default Name'),
        ),
        migrations.AddField(
            model_name='photocard',
            name='price',
            field=models.CharField(default='Default Price', max_length=200),
        ),
        migrations.AddField(
            model_name='photocard',
            name='type',
            field=models.TextField(default='Default Type'),
        ),
    ]
