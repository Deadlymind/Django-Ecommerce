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
        reviews = object.review_product.all().count()
        
        return reviews
    
    def get_avg_rate(self,object):
        total = 0 # sum rate : object
        reviews = object.review_product.all()


        if len(reviews) > 0:
            for item in reviews:
                total += item.rate
            
            avg = total / len(reviews)
        else:
            avg = 0
        return avg



class ProductReviewsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Review
        fields = ['user', 'review', 'rate', 'created_at']




class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    image = ProductImageSerializer(source='product_image',many=True)
    reviews = ProductReviewsSerializer(source='review_product',many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_review_count(self, object):
        reviews = object.review_product.all().count()
        return reviews
    

    
    def get_avg_rate(self,object):
        total = 0 # sum rate : object
        reviews = object.review_product.all()


        if len(reviews) > 0:
            for item in reviews:
                total += item.rate
            
            avg = total / len(reviews)
        else:
            avg = 0
        return avg
    




class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'