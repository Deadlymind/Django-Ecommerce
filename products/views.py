from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Brand, Review, ProductImage
from django.db.models import Q, F, Value, DecimalField
from django.db.models.aggregates import Count, Sum, Avg,Max,Min

# Create your views here.


def mydebug(request):
    # data = Product.objects.all() 

    # column number ---------------------
    # data = Product.objects.filter(price = 20)
    # data = Product.objects.filter(price__gt = 98)
    # data = Product.objects.filter(price__gte = 98)
    # data = Product.objects.filter(price__lt = 98)
    # data = Product.objects.filter(price__range = (80, 83))

    # relation ---------------------
    # data = Product.objects.filter(brand__id=5)
    # data = Product.objects.filter(brand__id__gt=600)

    # text ---------------------
    # data = Product.objects.filter(name__contains='iphone')
    # data = Product.objects.filter(name__startswith='ipho')
    # data = Product.objects.filter(name__endswith='one')
    # data = Product.objects.filter(price__isnull=True)

    # dates ---------------------
    # data = Product.objects.filter(date_column__year=2022)
    # data = Product.objects.filter(date_column__month=2)
    # data = Product.objects.filter(date_column__day=20)

    # complex queries ---------------------
    # data = Product.objects.filter(flag='New', price__gt=98)
    # data = Product.objects.filter(flag='New').filter(price__gt=98)

    # data = Product.objects.filter(
    #     Q(flag='New') &
    #     Q(price__gt=98)
    #     )

    # data = Product.objects.filter(
    # Q(flag='New') |
    # Q(price__gt=98)
    # )

    # Field Reference ---------------
    # data = Product.objects.filter(quantity=F('price'))
    # data = Product.objects.filter(quantity=F('category_id'))

    # Order ------------------
    # data = Product.objects.all().order_by('name') #ASCending
    # data = Product.objects.order_by('name') 
    # data = Product.objects.order_by('-name') #DEScending
    # data = Product.objects.order_by('-name', 'price')
    # data = Product.objects.filter(price__gt=80).order_by('name')
    # data = Product.objects.order_by('name')[:10]
    # data = Product.objects.earliest('name')
    # data = Product.objects.latest('name')

    # limit fields -----------------------
    # data = Product.objects.values('name', 'price')
    # data = Product.objects.values_list('name', 'price', 'brand')
    # data = Product.objects.only('name', 'price')
    # data = Product.objects.defer('description', 'subtitle')

    # select related --------------
    # data = Product.objects.select_related('brand').all() #foriegnkey, one-to-one
    # data = Product.objects.prefetch_related('brand').all() #many to many
    # data = Product.objects.select_related('brand').select_related('category').all()

    # aggregation Count, Min, Max, Sum, average ---------------------
    # data = Product.objects.aggregate(
    #     Avg('price'),
    #     Count('id')
    #     )
    
    # annotation ---------------
    # data = Product.objects.annotate(is_new=Value(0))
    data = Product.objects.annotate(price_with_tax=F('price'))















    return render(request, 'products/debug.html',{'data':data})





class ProductList(ListView):
    model = Product
    paginate_by = 100

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductImage.objects.filter(product=self.get_object())
        context['related'] = Product.objects.filter(brand=self.get_object().brand)
        return context


class BrandList(ListView):
    model = Brand
    paginate_by = 50


class BrandDetail(ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    paginate_by = 50



    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context





