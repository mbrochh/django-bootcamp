from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^shipping/',
        TemplateView.as_view(
            template_name='user_profiles/shipping_address_view.html'),
        name='user_profiles_shipping'),
]