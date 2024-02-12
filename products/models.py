from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category")
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return f"{self.product_id} product's image"


class Product(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self):
        return self.type


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="feedbacks")
    body = models.TextField()

    def __str__(self):
        return self.name


class OurWorks(models.Model):
    image = models.ImageField(upload_to="uploads")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
