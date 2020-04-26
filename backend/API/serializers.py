from rest_framework import serializers
from API.models import Product, User, Comment


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    rating = serializers.CharField()
    price = serializers.CharField()
    def create(self, validated_data):
        product = Product()
        product.name = validated_data.get('name')
        product.address = validated_data.get('address')
        product.description = validated_data.get('description')
        product.rating = validated_data.get('rating')
        product.save()
        return product
    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.description = validated_data.get('description', instance.description)
        instance.rating = validated_data.get('rating', instance.city)
        return instance
class UserSerializer(serializers.Serializer):
    password = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    status = serializers.CharField()
    comment = serializers.CharField()
    def create(self, validated_data):
        user = User()
        user.password = validated_data.get('password')
        user.username = validated_data.get('username')
        user.status = validated_data.get('status')
        user.comment = validated_data.get('comment')
        user.save()
        return user



