from django.contrib import admin

from shop.models import Product, Payment, OrderItem, Order
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Order)

