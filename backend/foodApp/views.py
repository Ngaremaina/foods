from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category,User, Customer, Admin, Location,Payment,Sales,Cart
from  .serializers import (ProductSerializer,CategorySerializer, UserSerializer,CustomerSerializer,AdminSerializer,LocationSerializer,PaymentSerializer,SalesSerializer,CartSerializer)

class  UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class  CategoryViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Category.objects.all().order_by('name')
  serializer_class=CategorySerializer
  
class   ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all( ).order_by('category','name')
  serializer_class=ProductSerializer
  
class  SalesViewSet(viewsets.ModelViewSet):
  queryset = Sales.objects.all()
  serializer_class = SalesSerializer

class  PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  
class LocationViewSet(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  
class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer
  
class AdminViewSet(viewsets.ModelViewSet):
  queryset = Admin.objects.all()
  serializer_class = AdminSerializer