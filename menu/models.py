from django.db import models

# Create your models here.

class MenuShow(models.Model):
    menu_img = models.ImageField(upload_to='imgmenu/', verbose_name='Фото блюда')
    menu_title = models.CharField(max_length=100, verbose_name='Название')
    menu_ingredients = models.CharField(max_length=300, verbose_name='Состав')
    menu_price = models.CharField(max_length=100, verbose_name='Цена, руб.')
    menu_category = models.CharField(max_length=100, verbose_name= 'Категория (salads, soup, hotter, grill)')
    menu_allergens = models.CharField(max_length=300, null=True, default='Нет', verbose_name='Наличие аллергенов')
    menu_kkal = models.CharField(max_length=100, null=True, default='0', verbose_name='Пищевая ценность Ккал')

    def __str__(self):
        return self.menu_title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'