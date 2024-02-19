import pytest

from .factories import CategoryFactory, ProductFactory


@pytest.mark.django_db
def test_get_categories(api_client):
    c = CategoryFactory()
    c2 = CategoryFactory()
    p1 = ProductFactory(category=c)
    p2 = ProductFactory(category=c)
    p3 = ProductFactory(category=c2)

    response = api_client.get("/api/products/categories/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert len(response.json()[0]["products"]) == 2
    assert len(response.json()[1]["products"]) == 1

    assert response.json()[0]["id"] == c.id
    assert response.json()[0]["description"] == c.description
    assert response.json()[0]["name"] == c.name
    assert c.image.url in response.json()[0]["image"]

    assert response.json()[1]["id"] == c2.id
    assert response.json()[1]["description"] == c2.description
    assert response.json()[1]["name"] == c2.name
    assert c2.image.url in response.json()[1]["image"]
