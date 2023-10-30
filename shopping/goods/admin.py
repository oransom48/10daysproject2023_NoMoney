from django.contrib import admin
from .models import Goods, Cart, Product, Ordered


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "quantity")


class GoodsAdmin(admin.ModelAdmin):
    list_display = ("goodsname", "id", "price")


class CartUser(admin.ModelAdmin):
    list_display = ("product_name", "price", "quantity")


class OrderedUser(admin.ModelAdmin):
    list_display = ("firstname", "datetime", "paid")


admin.site.register(Product, ProductAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Cart, CartUser)
admin.site.register(Ordered, OrderedUser)
