from rest_framework import serializers

from .models import MenuShow

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuShow
        fields = ('menu_img', 'menu_title', 'menu_ingredients', 'menu_price', 'menu_category', 'menu_allergens', 'menu_kkal')