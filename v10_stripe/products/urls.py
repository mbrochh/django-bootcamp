from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/',
        views.ProductsDetailView.as_view(),
        name='products_detail'),
]