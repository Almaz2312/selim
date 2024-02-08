from rest_framework import serializers

from .models import News, NewsImage


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ["id", "title", "body", "created_at", "updated_at", "images"]

    def create(self, validated_data):
        images_data = self.context.get("request").FILES.getlist("images")
        news = News.objects.create(**validated_data)
        for image_data in images_data:
            NewsImage.objects.create(news=news, image=image_data)
        return news
