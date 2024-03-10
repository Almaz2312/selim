from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewImageList, NewsList

urlpatterns = [
    path("news/", NewsList.as_view(), name="news"),
    path("news_image/", NewImageList.as_view(), name="news_image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
