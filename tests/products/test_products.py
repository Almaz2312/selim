import pytest

from products.models import Category, Product


@pytest.mark.django_db
def test_get_product_by_category(api_client):
    c = Category.objects.create(name="шлагбаум", description="test")
    p1 = Product.objects.create(type="ШЛАГБАУМЫ 1", description="test", category=c)
    p2 = Product.objects.create(type="ШЛАГБАУМЫ 2", description="test", category=c)
    response = api_client.get(f"/api/products/{c.name}")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_get_all_products(api_client):
    c = Category.objects.create(name="шлагбаум", description="test")
    p1 = Product.objects.create(type="ШЛАГБАУМЫ 1", description="test", category=c)
    p2 = Product.objects.create(type="ШЛАГБАУМЫ 2", description="test", category=c)
    response = api_client.get(f"/api/products/")
    assert response.status_code == 200
    assert len(response.json()) == 2
