from rest_framework import serializers
from taggit.serializers import TagListSerializerField,TaggitSerializer

from .models import Product, Brand, ProductImage, Review

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


  



class ProductReviewsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Review
        fields = ['user', 'review', 'rate', 'created_at']




class ProductDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    images = ProductImageSerializer(source='product_image',many=True)
    reviews = ProductReviewsSerializer(source='review_product',many=True)
    tags = TagListSerializerField()


    class Meta:
        model = Product
        fields = ['name', 'price', 'flag', 'image','subtitle', 'description','sku','tags','brand', 'review_count', 'avg_rate', 'reviews','images']







class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'