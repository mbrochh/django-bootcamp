from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    shipping_first_name = models.CharField(max_length=256, blank=True)
    shipping_last_name = models.CharField(max_length=256, blank=True)
    shipping_country = models.CharField(max_length=256, blank=True)
    shipping_state = models.CharField(max_length=256, blank=True)
    shipping_city = models.CharField(max_length=256, blank=True)
    shipping_street = models.CharField(max_length=256, blank=True)
    shipping_zip = models.CharField(max_length=256, blank=True)
    shipping_phone = models.CharField(max_length=256, blank=True)
    
    
@receiver(post_save, sender=User)
def user_post_save_handler(sender, **kwargs):
    if kwargs.get('created'):
        UserProfile.objects.create(user=kwargs.get('instance'))