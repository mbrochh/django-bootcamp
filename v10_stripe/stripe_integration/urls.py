from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^checkout/$',
        views.CheckoutView.as_view(),
        name='stripe_integration_checkout'),
    url(r'^success/$',
        views.SuccessView.as_view(),
        name='stripe_integration_success'),
]