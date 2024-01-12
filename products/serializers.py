from rest_framework import serializers
from .models import Product, Brand, ProductImage, Review

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()



    class Meta:
        model = Product
        fields = '__all__'

    def get_review_count(self, object):
        reviews = object.review_count()
        return reviews
    
    def get_avg_rate(self,object):
        avg = object.avg_rate()
        return avg



class ProductReviewsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Review
        fields = ['user', 'review', 'rate', 'created_at']




class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    image = ProductImageSerializer(source='product_image',many=True)
    reviews = ProductReviewsSerializer(source='review_product',many=True)

    class Meta:
        model = Product
        fields = '__all__'






class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'