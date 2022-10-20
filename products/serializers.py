from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Product, ProductOption, Tag


class TagSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Tag
        fields = ["id", "name"]


class ProductOptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = ProductOption
        fields = ["id", "name", "price"]


class ProductSerializer(WritableNestedModelSerializer):
    name = serializers.CharField()
    tag_set = TagSerializer(many=True)
    option_set = ProductOptionSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "tag_set", "option_set"]
