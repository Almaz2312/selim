from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductListView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
