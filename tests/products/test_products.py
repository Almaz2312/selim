import pytest
from rest_framework import serializers

from products.models import Category, Product


@pytest.mark.django_db
def test_get_product_by_category(api_client):
    c = Category.objects.create(name="шлагбаум", description="test")
    c2 = Category.objects.create(name="other", description="test")
    p1 = Product.objects.create(type="ШЛАГБАУМЫ 1", description="test", category=c)
    p2 = Product.objects.create(type="ШЛАГБАУМЫ 2", description="test", category=c)
    p3 = Product.objects.create(type="other", description="test", category=c2)
    response = api_client.get(f"/api/products/{c.name}/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["id"] == p1.id
    assert response.json()[0]["type"] == p1.type
    assert response.json()[0][
        "updated_at"
    ] == serializers.DateTimeField().to_representation(p1.updated_at)
    assert response.json()[0][
        "created_at"
    ] == serializers.DateTimeField().to_representation(p1.created_at)
    assert response.json()[0]["category"] == p1.category_id
    assert response.json()[0]["description"] == p1.description
    assert response.json()[1]["id"] == p2.id
    assert response.json()[1]["type"] == p2.type
    assert response.json()[1][
        "updated_at"
    ] == serializers.DateTimeField().to_representation(p2.updated_at)
    assert response.json()[1][
        "created_at"
    ] == serializers.DateTimeField().to_representation(p2.created_at)
    assert response.json()[1]["category"] == p2.category_id
    assert response.json()[1]["description"] == p2.description


@pytest.mark.django_db
def test_get_all_products(api_client):
    c = Category.objects.create(name="шлагбаум", description="test")
    p1 = Product.objects.create(type="ШЛАГБАУМЫ 1", description="test", category=c)
    p2 = Product.objects.create(type="ШЛАГБАУМЫ 2", description="test", category=c)
    response = api_client.get("/api/products/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["id"] == p1.id
    assert response.json()[0]["type"] == p1.type
    assert response.json()[0][
        "updated_at"
    ] == serializers.DateTimeField().to_representation(p1.updated_at)
    assert response.json()[0][
        "created_at"
    ] == serializers.DateTimeField().to_representation(p1.created_at)
    assert response.json()[0]["category"] == p1.category_id
    assert response.json()[0]["description"] == p1.description
    assert response.json()[1]["id"] == p2.id
    assert response.json()[1]["type"] == p2.type
    assert response.json()[1][
        "updated_at"
    ] == serializers.DateTimeField().to_representation(p2.updated_at)
    assert response.json()[1][
        "created_at"
    ] == serializers.DateTimeField().to_representation(p2.created_at)
    assert response.json()[1]["category"] == p2.category_id
    assert response.json()[1]["description"] == p2.description
