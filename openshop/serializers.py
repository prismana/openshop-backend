from openshop.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "shop", "location", "price", "discount", "category", "stock", "is_available", "picture"]