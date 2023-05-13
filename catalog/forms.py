from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_preview', 'category', 'purchase_price', 'creation_date',
                  'last_modified_date']
