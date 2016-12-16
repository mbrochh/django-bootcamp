from django import forms

from . import models


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'shipping_first_name',
            'shipping_last_name',
            'shipping_country',
            'shipping_city',
            'shipping_state',
            'shipping_street',
            'shipping_zip',
            'shipping_phone',
        ]
        
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.fields['shipping_first_name'].required = True
        self.fields['shipping_last_name'].required = True
        self.fields['shipping_country'].required = True
        self.fields['shipping_city'].required = True
        self.fields['shipping_state'].required = False
        self.fields['shipping_street'].required = True
        self.fields['shipping_zip'].required = True
        self.fields['shipping_phone'].required = True

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        return super(ShippingAddressForm, self).save(*args, **kwargs)