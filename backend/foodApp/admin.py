from django.contrib import admin
from .models import User, Customer, Admin, Category, Product, Location, Payment, Sales, Cart

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Payment)
admin.site.register(Sales)
admin.site.register(Cart)

