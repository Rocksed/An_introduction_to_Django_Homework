from django import forms
from catalog.models import Product, Blog


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_preview', 'category', 'purchase_price', 'creation_date',
                  'last_modified_date']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['headline', 'slug', 'content', 'preview', 'creation_date_blog', 'publication_feature',
                  'views_count']
