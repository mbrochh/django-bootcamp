from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')