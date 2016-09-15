from django.views import generic

from . import models


class ProductsListView(generic.TemplateView):
    template_name = 'products/products_list_view.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductsListView, self).get_context_data(**kwargs)
        ctx.update({
            'products': models.Product.objects.all(),
        })
        return ctx
        
        
class ProductsDetailView(generic.DetailView):
    template_name = 'products/products_detail_view.html'
    model = models.Product
    
    def get_context_data(self, **kwargs):
        self.request.session['product_id'] = self.object.pk
        return super(ProductsDetailView, self).get_context_data(**kwargs)