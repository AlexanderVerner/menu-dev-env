# Generated by Django 3.2.6 on 2021-08-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menushow',
            name='menu_img',
            field=models.ImageField(upload_to='imgmenu/', verbose_name='Фото блюда'),
        ),
        migrations.AlterField(
            model_name='menushow',
            name='menu_ingredients',
            field=models.CharField(max_length=300, verbose_name='Состав'),
        ),
        migrations.AlterField(
            model_name='menushow',
            name='menu_price',
            field=models.CharField(max_length=100, verbose_name='Цена, руб.'),
        ),
    ]