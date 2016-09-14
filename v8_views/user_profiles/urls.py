from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^shipping/',
        views.ShippingAddressView.as_view(),
        name='user_profiles_shipping'),
]