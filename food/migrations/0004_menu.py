# Generated by Django 5.0.4 on 2024-04-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_rename_reservation_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('item_price', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
