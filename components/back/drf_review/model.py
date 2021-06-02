from django.contrib import admin
from django.db import models
from django.utils import timezone

from django.conf import settings
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    stars = models.IntegerField(choices=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ))
    text = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f'{self.product_name} - {self.author} - {self.text}'

    def __str__(self):
        return f'{self.product_name} - {self.author} - {self.text}'


admin.site.register(Review)
