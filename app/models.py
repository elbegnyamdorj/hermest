from django.db import models

# Create your models here.class BestComputers:

class BestComputers(models.Model):
    name=models.TextField()
    prod_url=models.TextField()
    category = models.TextField()
    image_link = models.TextField()
    price = models.TextField()
class NewTech(models.Model):
    name=models.TextField()
    prod_url=models.TextField()
    category = models.TextField()
    image_link = models.TextField()
    price = models.TextField()
class HiTech(models.Model):
    name=models.TextField()
    prod_url=models.TextField()
    category = models.TextField()
    image_link = models.TextField()
    price = models.TextField()