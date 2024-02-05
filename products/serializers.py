from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        request = self.context["request"]
        return [request.build_absolute_uri(img.image.url) for img in obj.images.all()]

    class Meta:
        model = Product
        fields = "__all__"
