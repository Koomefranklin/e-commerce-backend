from rest_framework import serializers
from .models import Category, Product, Order, User, Cart
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.http import JsonResponse

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
        'id',
        'first_name',
        'last_name',
        'email',
        'username',
        'password',
        'last_name',
        'is_staff',
    ]
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
  
  def update(self, instance, validated_data):
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.email = validated_data.get('email', instance.email)
    instance.save()
    return instance

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = [
      'id',
      'name', 'description', 'created_at', 'updated_at'
    ]

  def create(self, validated_data):
    return Category.objects.create(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
  category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
  class Meta:
    model = Product
    fields = [
      'id',
      'name',
      'description',
      'price',
      'quantity_available',
      'image',
      'category',
      'created_at',
      'updated_at'
    ]

  def create(self, validated_data):
    return Product.objects.create(**validated_data)
  
class CartSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
  class Meta:
    model = Cart
    fields = [
      'id',
      'user',
      'product',
      'quantity',
      'created_at',
      'updated_at'
    ]

  def create(self, validated_data):
    user = self.context['request'].user
    product = validated_data.get('product')
    quantity = validated_data.get('quantity')
    cart_data = Cart.objects.filter(user=user, product=product).all()
    try:
      if not cart_data:
        data = {'user': user, 'product': product, 'quantity': quantity}
        cart_data = Cart.objects.create(**data)
      else:
        raise IntegrityError("The Product already exsist in your cart")
      return cart_data
    except IntegrityError as e:
      raise serializers.ValidationError(str(e))
  
  def update(self, instance, validated_data):
    instance.quantity = validated_data.get('quantity', instance.quantity)
    instance.save()
    return instance
  
class CartViewSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  product = ProductSerializer()
  class Meta:
    model = Cart
    fields = [
      'id',
      'user',
      'product',
      'quantity',
    ]

class OrderSerializer(serializers.ModelSerializer):
  cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
  class Meta:
    model = Order
    fields = [
      'id',
      'cart',
      'amount',
      'shipping_address',
      'payment_method',
      'created_at',
      'updated_at'
    ]

  def create(self, validated_data):
    return Order.objects.create(**validated_data)
