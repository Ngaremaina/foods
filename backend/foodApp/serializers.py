from rest_framework import serializers
from .models import User, Customer, Admin,Category,Cart,Product,Location,Payment,Sales

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields= ['id','role','email','password',]

class CustomerSerializer(serializers.ModelSerializer):
  class  Meta:
    model = Customer
    fields = ['id','firstname','lastname', 'phone','image']
    
class  AdminSerializer(UserSerializer):
  class Meta:
    model = Admin
    fields = ['id','user','username','firstname', 'lastname','phone']

class  CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id','name']
    
class  ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['id','name','description','price','image','category']
    
class PaymentSerializer(serializers.ModelSerializer):
  class  Meta:
    model = Payment
    fields = ['id','payment_type','payment_amount','payment_date','payment_time','payment_status']
    
class SalesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sales
    fields = ['id,''quantity','amount','name','payment']
    
class  CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    fields = ['id','name','price','description','image','quantity','total','product']
class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['id','user','address','city','country']
  