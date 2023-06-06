from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Blog, Version


class ProductVersion(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'purchase_price', 'image_preview']

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        name = self.cleaned_data['name'].lower()
        for word in forbidden_words:
            if word in name:
                raise ValidationError(f"Слово {word} не допускается в названии.")
        return name

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        description = self.cleaned_data['description'].lower()
        for word in forbidden_words:
            if word in description:
                raise ValidationError(f"Слово {word} не допускается в описании")
        return description


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['headline', 'content', 'preview', 'creation_date_blog']
        # fields = '__all__'
