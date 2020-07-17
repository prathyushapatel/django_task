from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    phonenum = models.CharField(max_length=13)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
