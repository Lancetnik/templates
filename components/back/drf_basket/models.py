from django.contrib import admin
from django.db import models

from django.conf import settings
from products.models import Product


class Basket(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __repr__(self): return f'Корзина {self.user}'
    def __str__(self): return f'Корзина {self.user}'


class BasketItem(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='in_basket'
    )
    basket = models.ForeignKey(
        Basket, 
        on_delete=models.CASCADE, 
        related_name='items'
    )

    def __repr__(self): 
        return f'Товар {self.product} в корзине {self.basket}'

    def __str__(self):
        return f'Товар {self.product} в корзине {self.basket}'


admin.site.register(Basket)
admin.site.register(BasketItem)
