from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductListView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductByCategory(APIView):
    def get(self, request, category):
        p = Product.objects.filter(category__name=category)
        return Response(ProductSerializer(p, many=True).data)
