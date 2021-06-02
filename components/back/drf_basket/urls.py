from django.urls import path

from . import views


urlpatterns = [
    path("add-item/", views.BasketItemCreateView.as_view()),
    path("delete-item/<int:pk>/", views.BasketItemDestroyView.as_view()),

    path("", views.GetBasket.as_view()),
    path("clear/", views.ClearBasket.as_view()),
]