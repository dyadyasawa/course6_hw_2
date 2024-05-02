
from django.urls import path
from catalog.views import ProductListView, ContactTemplateView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductUpdateIsPublishedView, ProductUpdateDescriptionView, ProductUpdateCategoryView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('contact/', ContactTemplateView.as_view(), name="contact"),
    path('product_1/<int:pk>', ProductDetailView.as_view(), name="product_1"),

    path('create_product/', ProductCreateView.as_view(), name="create_product"),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name="update_product"),

    path('update_product_is_published/<int:pk>/', ProductUpdateIsPublishedView.as_view(), name="update_product_is_published"),
    path('update_product_description/<int:pk>/', ProductUpdateDescriptionView.as_view(), name="update_product_description"),
    path('update_product_category/<int:pk>/', ProductUpdateCategoryView.as_view(), name="update_product_category"),

    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name="delete_product"),

    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('create/', BlogCreateView.as_view(), name="blog_create"),
    path('update/<int:pk>', BlogUpdateView.as_view(), name="blog_update"),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name="blog_delete"),

    # path('version_create/', VersionCreateView.as_view(), name="version_create"),
    # path('version_list/', VersionListView.as_view(), name="version_list"),
    # path('version_detail/<int:pk>', VersionDetailView.as_view(), name="version_detail"),
    # path('version_update/<int:pk>', VersionUpdateView.as_view(), name="version_update"),
    # path('version_delete/<int:pk>', VersionDeleteView.as_view(), name="version_delete")
]
