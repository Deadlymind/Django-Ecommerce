from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Brand, Review, ProductImage
from . import serializers
from .pagination import MyPagination



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'flag']


class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    


class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    pagination_class = MyPagination



class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    
