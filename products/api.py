from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .models import Product, Brand, Review, ProductImage
from . import serializers
from .pagination import MyPagination



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand', 'flag']
    search_fields = ['name', 'subtitle', 'description']


class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    


class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']




class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    
