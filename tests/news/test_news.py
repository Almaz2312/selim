import pytest

from news.factories import NewsFactory, NewsImageFactory


@pytest.mark.django_db
def test_news_factory():
    news_instance = NewsFactory(title="Test Title", body="Test Body")

    assert news_instance is not None

    assert news_instance.title == "Test Title"
    assert news_instance.body == "Test Body"


@pytest.mark.django_db
def test_news_image_factory():
    news_instance = NewsFactory()
    news_image_instance = NewsImageFactory(news=news_instance)

    assert news_image_instance is not None

    assert news_image_instance.title
    assert news_image_instance.image
    assert news_image_instance.news == news_instance
