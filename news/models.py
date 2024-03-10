from datetime import datetime

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250)  # type: ignore
    body = models.TextField()  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)  # type: ignore
    updated_at = models.DateTimeField(auto_now=True)  # type: ignore

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="images", default=None
    )  # type: ignore
    title = models.CharField(max_length=250)  # type: ignore
    image = models.ImageField(upload_to="news_images")

    def __str__(self) -> str:
        return self.title
