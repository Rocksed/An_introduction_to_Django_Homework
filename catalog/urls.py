from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, BlogListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index-hone'),
    path('contacts/', contacts, name='index-contacts'),
    path('blog/', BlogListView.as_view(), name='index-blog'),
]
