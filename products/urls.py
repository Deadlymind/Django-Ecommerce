from django.urls import path, include
from .views import ProductDetail, ProductList, BrandList, BrandDetail, mydebug

from . import api


urlpatterns = [
    path('debug', mydebug),
    path('brands', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),

    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),


    # api urls

    path('api/list', api.ProductListApi.as_view()),
    path('api/list/<int:pk>', api.ProductDetailApi.as_view()),

    path('api/brands', api.BrandListApi.as_view()),
    path('api/brands/<int:pk>', api.BrandDetailApi.as_view()),

]