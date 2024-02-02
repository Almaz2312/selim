from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category")
    description = models.TextField()


class Product(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="product",
    )


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="feedbacks")
    body = models.TextField()


class OurWorks(models.Model):
    image = models.ImageField(upload_to="uploads")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
