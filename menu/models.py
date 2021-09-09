from django.db import models

# Create your models here.

class MenuShow(models.Model):
    CATEGORY_CHOICES = [
        ('salads', 'Салат'),
        ('soup', 'Суп'),
        ('hotter', 'Горячее'),
        ('grill', 'Гриль'),
    ]
    menu_img = models.ImageField(upload_to='imgmenu/', verbose_name='Фото блюда')
    menu_title = models.CharField(max_length=100, verbose_name='Название')
    menu_ingredients = models.JSONField(verbose_name='Состав')
    menu_price = models.IntegerField(verbose_name='Цена, руб.')
    menu_category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория'
    )
    menu_allergens = models.CharField(max_length=300, null=True, default='Нет', verbose_name='Наличие аллергенов')
    menu_kkal = models.IntegerField(null=True, default=0, verbose_name='Пищевая ценность Ккал')

    def __str__(self):
        return self.menu_title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'