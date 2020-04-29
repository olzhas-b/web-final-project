from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()
    def to_json(self):
        return {
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.TextField(max_length=200)
    rating = models.FloatField(max_length=200)
    image = models.TextField()
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    ref = models.TextField()
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'image': self.image,
            'description': self.description,
            'ref': self.ref,
            'category_id': self.category_id
        }

class Feedback(models.Model):
    UsernameOrTelephoneNumber = models.TextField()
    Email = models.TextField()
    productID = models.IntegerField()
    Message = models.TextField()
    def to_json(self):
        return {
            'id': self.id,
            'UsernameOrTelephoneNumber': self.UsernameOrTelephoneNumber,
            'Email': self.Email,
            'productID': self.productID,
            'Message': self.Message,
        }

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Order(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()

class Comment(models.Model):
    username = models.CharField(max_length=200)
    body = models.CharField(max_length=200)







class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.TextField(max_length=200)
    rating = models.FloatField(max_length=200)
    image = models.TextField()
    description = models.TextField()
    category_id = models.IntegerField()
    ref = models.TextField()
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'image': self.image,
            'description': self.description,
            'ref': self.ref,
            'category_id': self.category_id
        }