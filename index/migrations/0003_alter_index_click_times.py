# Generated by Django 4.2.7 on 2023-11-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_index_click_times_index_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='click_times',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
