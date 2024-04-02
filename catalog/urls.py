
from django.urls import path
from catalog.views import ProductListView, ContactTemplateView, ProductDetailView, BlogCreateView, BlogListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('contact/', ContactTemplateView.as_view(), name="contact"),
    path('product_1/<int:pk>', ProductDetailView.as_view(), name="product_1"),
    path('blog', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name="blog_create")
]
