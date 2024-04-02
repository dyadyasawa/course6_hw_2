
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog_app/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog_app/contact.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_app/product_1.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))

        return queryset
