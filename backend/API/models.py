from django.db import models
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.CharField(max_length=200)
    price = models.TextField(max_length=200)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'rating': self.rating,
            'price': self.price
        }
class User(models.Model):
    password = models.CharField(max_length=200)
    username = models.TextField()
    status = models.FloatField()
    comment = models.ForeignKey(Company, on_delete=models.CASCADE)
    def to_json(self):
        return {
            'id': self.id,
            'password': self.password,
            'username': self.username,
            'status': self.status
        }
class Comment(models.Model):
    user_id = models.TextField()
    body = models.TextField()
    date = model.TextField()
    like = model.FloatField()
    def to_json(self):
        return {
            'user_id': self.user_id,
            'body': self.body,
            'date': self.date,
            'like': self.like
        }
class Test(models.Model):
    title = models.CharField(max_length=100)



