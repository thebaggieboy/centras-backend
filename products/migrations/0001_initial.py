# Generated by Django 3.2.5 on 2024-08-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=250, null=True)),
                ('category', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]