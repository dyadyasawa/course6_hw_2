
from django.urls import path
from catalog.views import ProductListView, ContactTemplateView, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('contact/', ContactTemplateView.as_view(), name="contact"),
    path('product_1/<int:pk>', ProductDetailView.as_view(), name="product_1"),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('create/', BlogCreateView.as_view(), name="blog_create")
]
