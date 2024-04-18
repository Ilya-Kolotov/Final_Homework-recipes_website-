# Generated by Django 5.0.2 on 2024-02-25 05:18

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
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('nick_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('about_me', models.TextField()),
                ('register_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cooking_time', models.DecimalField(decimal_places=2, max_digits=10)),
                ('images', models.ImageField(blank=True, null=True, upload_to='dish_images/')),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=models.SET('Вне категорий'), to='myapp.category')),
                ('chef_id', models.ForeignKey(on_delete=models.SET('Анонимный шеф-повар'), to='myapp.chef')),
            ],
        ),
        migrations.CreateModel(
            name='CookingStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='dish_images/')),
                ('post_id', models.ManyToManyField(to='myapp.post')),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('measurement', models.CharField(choices=[('кг', 'килограмм'), ('литр', 'литр'), ('грамм', 'грамм'), ('столовая ложка', 'столовая ложка'), ('стакан', 'стакан'), ('чайная ложка', 'чайная ложка')], max_length=20)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]