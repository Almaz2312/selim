from django_filters import rest_framework as filters  # type: ignore
from rest_framework.generics import ListAPIView  # type: ignore

from .filters import ProductFilter
from .models import Category, Feedback, Product
from .serializers import CategorySerializer, FeedbackListSerializer, ProductSerializer


class CategoryListView(ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FeedbackListView(ListAPIView):
    model = Feedback
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer


class ProductListView(ListAPIView):
    model = Product
    queryset = Product.objects.all().prefetch_related("images")
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
