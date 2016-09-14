from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/',
        TemplateView.as_view(template_name='products/products_detail_view.html'),
        name='products_detail'),
]