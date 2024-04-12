from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm
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


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog_app/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class BlogListView(ListView):
    model = Blog
    template_name = 'catalog_app/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'catalog_app/blog_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))

        return queryset

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'catalog_app/blog_form.html'
    fields = ('title', 'body', 'preview', 'publication_sign', 'view_count',)
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'catalog_app/blog_form.html'
    fields = ('title', 'body', 'preview', 'publication_sign', 'view_count',)
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'catalog_app/blog_confirm_delete.html'
    success_url = reverse_lazy('catalog:blog_list')
