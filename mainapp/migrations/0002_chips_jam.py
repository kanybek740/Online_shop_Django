# Generated by Django 3.1.7 on 2021-02-27 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименовании')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображения')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('country_product', models.CharField(max_length=255, verbose_name='Strana proizvoditel')),
                ('taste', models.CharField(max_length=255, verbose_name='Vkus')),
                ('sort', models.CharField(max_length=255, verbose_name='sort_yabloki')),
                ('upakovka', models.CharField(max_length=255, verbose_name='Upakovka')),
                ('weight', models.PositiveIntegerField(default=0)),
                ('Kalorii', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категорий')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Chips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименовании')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображения')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('country_product', models.CharField(max_length=255, verbose_name='Strana proizvoditel')),
                ('taste', models.CharField(max_length=255, verbose_name='Vkus')),
                ('sort', models.CharField(max_length=255, verbose_name='sort_yabloki')),
                ('upakovka', models.CharField(max_length=255, verbose_name='Upakovka')),
                ('weight', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категорий')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
