import pytest

from .factories import FeedbackFactory


@pytest.mark.django_db
def test_get_feedbacks(api_client):
    f1 = FeedbackFactory()
    f2 = FeedbackFactory()

    response = api_client.get("/api/products/feedbacks/")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == f1.name
    assert response.json()[0]["id"] == f1.id
    assert response.json()[0]["type"] == f1.type_id
    assert response.json()[0]["body"] == f1.body
    assert f1.image.url in response.json()[0]["image"]

    assert response.json()[1]["name"] == f2.name
    assert response.json()[1]["id"] == f2.id
    assert response.json()[1]["type"] == f2.type_id
    assert response.json()[1]["body"] == f2.body
    assert f2.image.url in response.json()[1]["image"]
