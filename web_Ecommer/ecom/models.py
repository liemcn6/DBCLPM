from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='images', default=None,null=True)


class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ["-id"]
        unique_together = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='images', default=None,null=True)
    quantity = models.IntegerField()
    Rating = models.FloatField(default=0)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    NumReview = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        unique_together = ['name']


class Publisher(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        unique_together = ['name']


class Author(models.Model):
    name = models.CharField(max_length=40)
    dob = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        unique_together = ['name']


class Brand(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        unique_together = ['name']


class Laptop(Product):
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    cpu = models.CharField(max_length=40)
    ram = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Book(Product):
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    year = models.DateField()

    def __str__(self):
        return self.name


class Shoe(Product):
    Brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    material = models.CharField(max_length=100)
    size= models.IntegerField(null=True)

    def __str__(self):
        return self.name
class Cart(models.Model):
    name = models.CharField(max_length=100,default="")
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    total= models.FloatField(default=0)
    def __str__(self):
        return self.name

class CartItem(models.Model):
    Product = models.ForeignKey(Product ,related_name="product",on_delete=models.SET_NULL,null=True)
    Cart = models.ForeignKey(Cart,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.id

class Order(models.Model):
    User = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    total= models.FloatField(default=0)
    code=models.CharField(max_length=20,default=None)
    username = models.CharField(max_length=30, default=None)
    address = models.CharField(max_length=100, default=None)
    date=models.CharField(max_length=20,default=None);
    phone = models.CharField(max_length=10, default=None)
    content = models.CharField(max_length=10, default=None)
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.User

class OrderItem(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0)
    code=models.CharField(max_length=20,default=None)
    def __str__(self):
        return self.id
