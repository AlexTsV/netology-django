from django.db import models

# Create your models here.


class Phone(models.Model):
    manufacturer = models.TextField()
    model = models.TextField()
    price = models.TextField()
    OS = models.TextField()
    screen = models.TextField()
    camera = models.TextField()
    RAM = models.TextField()


class Samsung(models.Model):
    other = models.TextField()
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)


class Apple(models.Model):
    other = models.TextField()
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)


class Xiaomi(models.Model):
    other = models.TextField()
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)