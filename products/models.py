from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
 
 
@receiver(post_save, sender=User)
def user_post_save_handler(sender, **kwargs):
    if kwargs.get('created'):
        UserProfile.objects.create(user=kwargs.get('instance'))