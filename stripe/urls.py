from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^checkout/$',
        TemplateView.as_view(
            template_name='stripe/checkout_view.html'),
        name='stripe_checkout'),
    url(r'^success/$',
        TemplateView.as_view(
            template_name='stripe/success_view.html'),
        name='stripe_success'),
]
