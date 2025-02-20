from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, BlogForm, ProductIsPublishedForm, ProductDescriptionForm, \
    ProductCategoryForm
from catalog.models import Product, Blog, Version, Category
from catalog.services import get_categories_from_cache


class ProductListView(ListView):
    model = Product
    template_name = 'catalog_app/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog_app/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        # print(name, phone_number, message)
        return HttpResponseRedirect('/contact/')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog_app/product_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))

        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):

        product = form.save()
        product.creator = self.request.user
        product.save()

        context_data = self.get_context_data()
        formset = context_data['formset']

        if formset.is_valid():
            formset.instance = product
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object

    def test_func(self):
        product = self.get_object()
        user =self.request.user
        return product.creator == user or user.is_superuser

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if formset.is_valid():
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog_app/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateIsPublishedView(UpdateView, PermissionRequiredMixin):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductIsPublishedForm
    permission_required = ('Can change product published status',)

    success_url = reverse_lazy('catalog:home')


class ProductUpdateDescriptionView(UpdateView, PermissionRequiredMixin):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductDescriptionForm
    permission_required = ('Can change product description',)

    success_url = reverse_lazy('catalog:home')


class ProductUpdateCategoryView(UpdateView, PermissionRequiredMixin):
    model = Product
    template_name = 'catalog_app/product_form.html'
    form_class = ProductCategoryForm
    permission_required = ('Can change product category',)

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


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'catalog_app/blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
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


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'catalog_app/blog_confirm_delete.html'
    success_url = reverse_lazy('catalog:blog_list')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog_app/version_form.html'
    success_url = reverse_lazy('catalog:version_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog_app/version_form.html'
    success_url = reverse_lazy('catalog:version_list')


class CategoriesListView(ListView):
    model = Category
    template_name = 'catalog_app/categories_list.html'

    def get_queryset(self):
        return get_categories_from_cache()
