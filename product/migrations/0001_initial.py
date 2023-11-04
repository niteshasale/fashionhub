# Generated by Django 3.0.8 on 2021-01-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pant_type', models.CharField(choices=[('FORMAL', 'formal'), ('CASUAL', 'casual'), ('JEANS', 'jeans')], max_length=10)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.ImageField(upload_to='pant_photo')),
                ('status', models.CharField(choices=[('REGULAR', 'regular'), ('TREND', 'trend'), ('TODAYS DEAL', 'todays deal')], max_length=12)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('shirt_type', models.CharField(choices=[('FORMAL', 'formal'), ('CASUAL', 'casual'), ('HOODIE', 'hoodie')], max_length=10)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.ImageField(upload_to='shirt_photo')),
                ('status', models.CharField(choices=[('REGULAR', 'regular'), ('TREND', 'trend'), ('TODAYS DEAL', 'todays deal')], max_length=12)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('shoe_type', models.CharField(choices=[('FORMAL', 'formal'), ('CANVAS', 'canvas'), ('LOFER', 'lofer'), ('SNEAKERS', 'sneakers')], max_length=10)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.ImageField(upload_to='shoe_photo')),
                ('status', models.CharField(choices=[('REGULAR', 'regular'), ('TREND', 'trend'), ('TODAYS DEAL', 'todays deal')], max_length=12)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]
