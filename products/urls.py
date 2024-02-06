from django.urls import path

from .views import FeedbackListView, ProductByCategory, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("feedbacks/", FeedbackListView.as_view(), name="feedbacks"),
    path("<str:category>/", ProductByCategory.as_view(), name="product_by_category"),
]
