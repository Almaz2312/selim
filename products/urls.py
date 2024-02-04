from django.contrib import admin
from django.urls import path

from .views import ProductByCategory, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<str:category>", ProductByCategory.as_view(), name="product_by_category"),
]
