from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=100,null=True)
class Categories(models.Model):
    category_name=models.CharField(max_length=200,null=False)
    description=models.CharField(max_length=300,null=True)
    image = models.ImageField()
    class Meta:
        verbose_name = ("Kategoriyalar")
        verbose_name_plural = ("Kategoriyalar")

    def __str__(self):
        return self.category_name
class Products(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200,null=False)
    price=models.FloatField(null=False)
    image=models.ImageField()
    class Meta:
        verbose_name = ('Tovarlar')
        verbose_name_plural = ("Tovarlar")
    def __str__(self):
        return self.product_name
    @property
    def ImageURl(self):
            try:
                url=self.image.url
            except:
                url = 'rasm yoq'
            return url
   
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    order_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ('Buyurtmalar')
        verbose_name_plural = ("Buyurtmalar")
class Order_details(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    class Meta:
        verbose_name = ('Buyurtmalar tavsiliti')
        verbose_name_plural = ("Buyurtmalar tavsiloti")
    @property
    def get_total(self):
        return self.quantity * self.product.price




