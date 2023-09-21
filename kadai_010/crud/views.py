from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product
    fields = '__all__'
