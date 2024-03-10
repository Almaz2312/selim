from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import News, NewsImage
from .serializers import NewsImageSerializer, NewsSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewImageList(generics.ListAPIView):
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer
