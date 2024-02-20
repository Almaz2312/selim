from django.urls import path

from .views import CategoryListView, FeedbackListView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("feedbacks/", FeedbackListView.as_view(), name="feedbacks"),
    path("categories/", CategoryListView.as_view(), name="categories_list"),
]
