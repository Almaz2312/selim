import pytest

from products.models import Feedback


@pytest.mark.django_db
def test_get_feedbacks(api_client):
    f = Feedback.objects.create(name="asan", type="rolls", body="cool")
    f2 = Feedback.objects.create(name="asan", type="rolls", body="cool")
    response = api_client.get("/api/products/feedbacks/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == f.name
    assert response.json()[0]["id"] == f.id
    assert response.json()[0]["type"] == f.type
    assert response.json()[0]["body"] == f.body
    assert response.json()[1]["name"] == f2.name
    assert response.json()[1]["id"] == f2.id
    assert response.json()[1]["type"] == f2.type
    assert response.json()[1]["body"] == f2.body
