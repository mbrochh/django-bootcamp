from django.db import models


class UserProfile(models.Model):
    user = models.OneTo('auth.User')
    shipping_first_name = models.CharField(max_length=256, blank=True)
    shipping_last_name = models.CharField(max_length=256, blank=True)
    shipping_country = models.CharField(max_length=256, blank=True)
    shipping_state = models.CharField(max_length=256, blank=True)
    shipping_city = models.CharField(max_length=256, blank=True)
    shipping_street = models.CharField(max_length=256, blank=True)
    shipping_zip = models.CharField(max_length=256, blank=True)
    shipping_phone = models.CharField(max_length=256, blank=True)