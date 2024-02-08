import pytest
from rest_framework import serializers

from products.models import Category, Product


@pytest.mark.django_db
def test_get_categories(api_client):
    c = Category.objects.create(name="шлагбаум", description="test")
    c2 = Category.objects.create(name="other", description="test")
    p1 = Product.objects.create(type="ШЛАГБАУМЫ 1", description="test", category=c)
    p2 = Product.objects.create(type="ШЛАГБАУМЫ 2", description="test", category=c)
    p3 = Product.objects.create(type="other", description="test", category=c2)

    response = api_client.get("/api/products/categories/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert len(response.json()[0]["products"]) == 2
    assert len(response.json()[1]["products"]) == 1

    assert response.json()[0]["id"] == c.id
    assert response.json()[0]["description"] == c.description
    assert response.json()[0]["name"] == c.name
    assert response.json()[0]["image"] == serializers.ImageField().to_representation(
        c.image
    )
    assert response.json()[1]["id"] == c2.id
    assert response.json()[1]["description"] == c2.description
    assert response.json()[1]["name"] == c2.name
    assert response.json()[1]["image"] == serializers.ImageField().to_representation(
        c2.image
    )
