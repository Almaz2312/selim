from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from .models import News, NewsImage
from .views import NewImageList, NewsList


class NewsTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        # user = User.objects.create_user('admin', 'admin@example.com', 'password')
        news = [
            News(body="new news", title="new1"),
            News(body="new news1", title="new2"),
        ]
        News.objects.bulk_create(news)

    def test_list(self):
        request = self.factory.get("api/v1/news/")
        view = NewsList.as_view()
        response = view(request)

        # print(response.data)

        assert response.status_code == 200


class NewsImageTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        # user = User.objects.create_user('admin', 'admin@example.com', 'password')
        self.news = News.objects.create(title="Test News", body="Lorem ipsum")
        new_image = [
            NewsImage(news=self.news, image="test_image.jpg", title="abc"),
            NewsImage(news=self.news, image="test1_image.jpg", title="abc1"),
        ]
        NewsImage.objects.bulk_create(new_image)

    def test_list(self):
        request = self.factory.get("api/v1/news_image/")
        view = NewImageList.as_view()
        response = view(request)

        # print(response.data)

        assert response.status_code == 200
