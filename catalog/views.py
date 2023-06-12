from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from catalog.forms import ProductForm, BlogForm, ProductVersion
from catalog.models import Product, Blog, Version


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_form')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_formset.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:product_formset', args=[self.get_object().pk])

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().is_editable_by(request.user):
            # Если пользователь не является владельцем продукта, перенаправляем на другую страницу или выводим ошибку
            return HttpResponseForbidden("Вы не являетесь владельцем данного продукта.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=ProductVersion, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


########################################################################################################################
"""механизм CRUD для блога"""


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Увеличить количество просмотров на 1
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    # fields = ['headline', 'content', 'preview', 'creation_date_blog']
    form_class = BlogForm
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    form_class = BlogForm
    # fields = ['headline', 'content', 'preview', 'creation_date_blog']
    success_url = reverse_lazy('catalog:blog_list')


class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


########################################################################################################################
"""Контактная информация"""


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        phone = request.POST.get('Phone')
        print(f'User_name: {name}, User_email: {email}, User_massage:{massage}, User_phone: {phone}')
    return render(request, 'catalog/index-contacts.html', )
