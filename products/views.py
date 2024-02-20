from typing import Any
from django.shortcuts import get_object_or_404

from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Product, Brand, Review, ProductImage
from django.db.models import Q, F, Value, DecimalField, ExpressionWrapper
from django.db.models.aggregates import Count, Sum, Avg,Max,Min
from django.views.decorators.cache import cache_page


# Create your views here.

@cache_page(60 * 1)
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
    # data = Product.objects.annotate(
    # price_with_tax=ExpressionWrapper(F('price') * 1.15, output_field=DecimalField())
    # )

    data = Product.objects.all()
















    return render(request, 'products/debug.html',{'data':data})





class ProductList(ListView):
    model = Product
    paginate_by = 48

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(quantity__gt=0)
    #     return queryset


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
    queryset =Brand.objects.annotate(product_count=Count('product_brand'))




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
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context




# def add_review(request,slug):
#     product = Product.objects.get(slug=slug)

#     review = request.POST['review'] 

#     rate = request.POST['rating']

#     # add review

#     Review.objects.create(
#         user = request.user,
#         product = product,
#         review = review,
#         rate = rate
#     )

#     return redirect(f'/products/{slug}')


def add_review(request, slug):
    # Use get_object_or_404 to handle the case where the product does not exist.
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        review = request.POST.get('review', '')
        rate = request.POST.get('rating', '')

        if review and rate:  # Check if review and rate are not empty before proceeding.
            # Add review
            Review.objects.create(
                user=request.user,
                product=product,
                review=review,
                rate=rate
            )

    # Redirect to the product detail page.
    # return redirect('product_detail', slug=slug)
    return redirect(f'/products/{slug}')


