from django.urls import path, include
from .views import ProductDetail, ProductList


urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
]