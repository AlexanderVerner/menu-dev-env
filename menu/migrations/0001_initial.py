# Generated by Django 3.2.6 on 2021-08-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_img', models.ImageField(upload_to='imgmenu/')),
                ('menu_title', models.CharField(max_length=100, verbose_name='Название')),
                ('menu_ingredients', models.CharField(max_length=100, verbose_name='Состав')),
                ('menu_price', models.CharField(max_length=100, verbose_name='Цена')),
                ('menu_category', models.CharField(max_length=100, verbose_name='Категория (salads, soup, hotter, grill)')),
                ('menu_allergens', models.CharField(default='Нет', max_length=300, null=True, verbose_name='Наличие аллергенов')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]