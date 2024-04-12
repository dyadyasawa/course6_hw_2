
from django.urls import path
from catalog.views import ProductListView, ContactTemplateView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('contact/', ContactTemplateView.as_view(), name="contact"),
    path('product_1/<int:pk>', ProductDetailView.as_view(), name="product_1"),

    path('create_product/', ProductCreateView.as_view(), name="create_product"),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name="update_product"),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name="delete_product"),

    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('create/', BlogCreateView.as_view(), name="blog_create"),
    path('update/<int:pk>', BlogUpdateView.as_view(), name="blog_update"),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name="blog_delete")
]
