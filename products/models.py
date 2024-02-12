from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category")
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return f"{self.product_id} product's image"

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"


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

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="feedbacks")
    body = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class OurWorks(models.Model):
    image = models.ImageField(upload_to="uploads")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Наша работа"
        verbose_name_plural = "Наши работы"
