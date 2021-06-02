from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from .models import BasketItem, Basket
from .serializers import BasketItemSerializer, BasketSerializer


class BasketItemCreateView(generics.CreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

    def create(self, request, *args, **kwargs):
        basket = get_user_basket(self, self.get_queryset())
        data = dict(request.data)
        data['basket'] = basket

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BasketItemDestroyView(generics.DestroyAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        basket = get_user_basket(self, queryset)

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, basket=basket, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class ClearBasket(APIView):
    def delete(self, request, *args, **kwargs):
        basket = get_user_basket(self, Basket.objects.all())
        basket.items.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetBasket(generics.RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return get_user_basket(self, queryset)


def get_user_basket(self, queryset) -> Basket:
    if type(self.request.user) == AnonymousUser:
            self.permission_denied(
                self.request,
                code=status.HTTP_401_UNAUTHORIZED
            )
    basket, isCreated = queryset.get_or_create(user=self.request.user)
    return basket