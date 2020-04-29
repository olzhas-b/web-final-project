from rest_framework import serializers
from API.models import Products, Category, Feedback, User, Comment, Order


class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.CharField()
    rating = serializers.CharField()
    image = serializers.CharField()
    description = serializers.CharField()
    category_id = serializers.IntegerField()
    ref = serializers.CharField()

    def create(self, validated_data):
        products = Products()
        products.name = validated_data.get('name')
        products.price = validated_data.get('price')
        products.rating = validated_data.get('rating')
        products.image = validated_data.get('image')
        products.description = validated_data.get('description')
        products.category_id = validated_data.get('category_id')
        products.ref = validated_data.get('ref')
        products.save()
        return products
    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.ref = validated_data.get('ref', instance.ref)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    def create(self, validated_data):
        category = Category()
        category.name = validated_data.get('name')
        category.save()
        return  category
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class FeedBackSerializer(serializers.Serializer):
    UsernameOrTelephoneNumber = serializers.CharField()
    Email = serializers.CharField()
    productID = serializers.IntegerField()
    Message = serializers.CharField()
    id = serializers.IntegerField(read_only=True)
    def create(self, validated_data):
        feedback = Feedback()
        feedback.UsernameOrTelephoneNumber = validated_data.get('UsernameOrTelephoneNumber')
        feedback.Email = validated_data.get('Email')
        feedback.Message = validated_data.get('Message')
        feedback.productID = validated_data.get('productID')
        feedback.save()
        return feedback

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def create(self, validated_data):
        user = User()
        user.username = validated_data.get('username')
        user.password = validated_data.get('password')
        user.save()
        return user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class OrderSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    def create(self, validated_data):
        order = Order()
        order.user_id = validated_data.get('user_id')
        order.product_id = validated_data.get('product_id')
        return order
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    body = serializers.CharField()
    username = serializers.CharField()
    def create(self, validated_data):
        comment = Comment()
        comment.body = validated_data.get('body')
        comment.username = validated_data.get('username')
        comment.save()
        return comment
