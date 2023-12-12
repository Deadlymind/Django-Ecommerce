from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Brand, Review

# Create your views here.


class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product