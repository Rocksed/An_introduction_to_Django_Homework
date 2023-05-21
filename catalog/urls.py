from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index-home'),
    path('contacts/', contacts, name='index-contacts'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='block_form'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='block_form'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_confirm_delete'),
]


