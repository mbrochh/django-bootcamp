from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^checkout/$',
        TemplateView.as_view(
            template_name='stripe_integration/checkout_view.html'),
        name='stripe_checkout'),
    url(r'^success/$',
        TemplateView.as_view(
            template_name='stripe_integration/success_view.html'),
        name='stripe_success'),
]
