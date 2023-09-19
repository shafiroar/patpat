# Generated by Django 4.2.5 on 2023-09-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('pet', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
