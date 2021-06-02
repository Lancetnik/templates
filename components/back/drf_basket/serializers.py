from rest_framework import serializers

from products.serializers import DetailProductSerializer
from .models import BasketItem, Basket


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        exclude = ['id']


class BasketProductSerializer(DetailProductSerializer):
    pass


class DetailItemField(serializers.RelatedField):
    def to_representation(self, value):
        return BasketProductSerializer(value.product).data


class BasketSerializer(serializers.ModelSerializer):
    items = DetailItemField(read_only=True, many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Basket
        fields = '__all__'