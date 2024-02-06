from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback, Product
from .serializers import FeedbackListSerializer, ProductSerializer


class FeedbackListView(ListAPIView):
    model = Feedback
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer


class ProductListView(APIView):
    def get(self, request):
        p = Product.objects.all().prefetch_related("images")

        return Response(
            ProductSerializer(p, many=True, context={"request": request}).data
        )


class ProductByCategory(APIView):
    def get(self, request, category):
        p = Product.objects.filter(category__name=category).prefetch_related("images")

        return Response(
            ProductSerializer(p, many=True, context={"request": request}).data
        )
