from rest_framework import serializers
from .models import Categorys,Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorys
        fields=('id','category')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=('id','category','product_name','price')