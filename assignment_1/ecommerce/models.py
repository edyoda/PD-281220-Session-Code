from django.db import models

# Create your models here.)
class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.price)


class Order(models.Model):
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return "Order Id : {}".format(self.id)
