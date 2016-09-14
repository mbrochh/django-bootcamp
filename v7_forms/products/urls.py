from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<slug>[a-z-_]+)/',
        TemplateView.as_view(template_name='products/product_detail.html'),
        name='products_detail'),
]