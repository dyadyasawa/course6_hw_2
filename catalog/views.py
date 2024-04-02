from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


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


class BlogListView(ListView):
    model = Blog
    template_name = 'catalog_app/blog.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'catalog_app/blog_form.html'
    fields = ('title', 'body', 'preview', 'publication_sign', 'view_count',)
    success_url = reverse_lazy('catalog:blog')
