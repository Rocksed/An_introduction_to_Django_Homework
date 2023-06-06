from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_form'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_formset'),
    path('contacts/', contacts, name='index-contacts'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='block_form'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='block_form'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_confirm_delete'),
]
