from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  def __str__(self):
    return self.username
  pass

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  price = models.CharField(max_length=10)
  quantity_available = models.CharField(max_length=100)
  image = models.CharField(max_length=255)
  category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Cart(models.Model):
  user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
  quantity = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  models.UniqueConstraint(fields=['user', 'product'], name='unique_product_cart')

class Order(models.Model):
  cart = models.OneToOneField(Cart, verbose_name='Cart', on_delete=models.CASCADE)
  amount = models.CharField(max_length=10)
  shipping_address = models.CharField(max_length=100)
  payment_method = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
