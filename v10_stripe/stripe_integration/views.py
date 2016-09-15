from django.conf import settings
from django.views import generic
from django.shortcuts import redirect

import stripe

from products.models import Product


class CheckoutView(generic.TemplateView):
    template_name = 'stripe_integration/checkout_view.html'
    
    def dispatch(self, request, *args, **kwargs):
        product_id = request.session.get('product_id')
        if not product_id:
            return redirect('/')
        self.product = Product.objects.get(pk=product_id)
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        ctx.update({
           'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
           'amount': int(self.product.price * 100),
           'title': self.product.title,
        })
        return ctx
        
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        amount = request.POST.get('amount')
        profile = request.user.profile
        stripe.Charge.create(
            amount=amount,
            currency='sgd',
            source=token,
            description="Credit Card Payment to Django Bootcamp",
            shipping={
                'address': {
                    'city': profile.shipping_city,
                    'country': 'SG',
                    'line1': profile.shipping_street,
                    'postal_code': profile.shipping_zip,
                    'state': profile.shipping_state,
                },
                'name': '{} {}'.format(
                    profile.shipping_first_name, profile.shipping_last_name),
                'phone': profile.shipping_phone,
            }
        )
        return redirect('stripe_integration_success')        
    

class SuccessView(generic.TemplateView):
    template_name = 'stripe_integration/success_view.html'