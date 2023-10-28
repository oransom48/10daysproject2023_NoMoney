from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Goods(models.Model):
    image = models.ImageField(upload_to='image')
    goodsname = models.CharField(max_length=255)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=2200, null=True)

    def __str__(self):
        return f"{self.goodsname}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    sum_price = models.FloatField(null=True) 
    # I added this column because first I want price * quantity, but it couldn't. And I don't know why? Maybe Float can't * with Integer

    def __str__(self):
        return f"{self.quantity} x {self.product_id}"

    def get_absolute_url(self):
        return reverse("cart_detail")

# for ordered page
# I use ManyToMany Relationship, which likes Composition (or Aggregation? I'm not sure) in OOP.
class Product(models.Model):
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    sum_price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"

class Ordered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Cart
    products = models.ManyToManyField(Product)
    total_price = models.FloatField(null=True)

    #Additional information
    firstname = models.CharField(max_length=31, null=True)
    lastname = models.CharField(max_length=31, null=True)
    address = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=10, null=True)
    paid = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname}"