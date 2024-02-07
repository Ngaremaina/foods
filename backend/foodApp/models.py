from django.db import models

class User(models.Model):
    role = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
  
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
  
class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=100)
  
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
class Payment(models.Model):
    payment_type = models.CharField(max_length=50)
    payment_amount = models.IntegerField()
    payment_date = models.DateField()
    payment_time = models.DateTimeField()
    payment_status = models.CharField(max_length=50)
  
class Sales(models.Model):
    quantity = models.IntegerField()
    amount = models.IntegerField()
    name = models.CharField(max_length=100)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
  
class Cart(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()
    total = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
