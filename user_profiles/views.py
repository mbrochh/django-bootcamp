from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils.decorators import method_decorator

from . import forms
from . import models


class ShippingAddressView(generic.UpdateView):
    template_name = 'user_profiles/shipping_address_view.html'
    form_class = forms.ShippingAddressForm
    model = models.UserProfile

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(ShippingAddressView, self).dispatch(
            request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ShippingAddressView, self).get_form_kwargs()
        kwargs.update({
           'user': self.request.user,
        })
        return kwargs

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return '/stripe/checkout/'
