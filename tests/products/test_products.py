import pytest
from rest_framework import serializers

from .factories import CategoryFactory, ProductFactory


@pytest.mark.django_db
def test_get_product_by_category(api_client):
    c = CategoryFactory()
    c2 = CategoryFactory()

    p1 = ProductFactory(category=c)
    p2 = ProductFactory(category=c)
    p3 = ProductFactory()

    response = api_client.get(f"/api/products/?category={c.name}")
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
    assert len(response.json()[0]["images"]) == len(p1.images.all())
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
    assert len(response.json()[1]["images"]) == len(p2.images.all())


@pytest.mark.django_db
def test_get_all_products(api_client):
    p1 = ProductFactory()
    p2 = ProductFactory()

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
    assert len(response.json()[0]["images"]) == len(p1.images.all())
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
    assert len(response.json()[1]["images"]) == len(p2.images.all())
