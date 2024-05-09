# Generated by Django 5.0.6 on 2024-05-09 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50)),
                ('dish_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
            ],
        ),
    ]
