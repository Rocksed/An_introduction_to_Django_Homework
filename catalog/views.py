from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import ProductForm
from catalog.models import Product, Blog


def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    context = {
        'object_list': Product.objects.all(),
        'form': form,
    }
    return render(request, 'catalog/index-home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        phone = request.POST.get('Phone')
        print(f'User_name: {name}, User_email: {email}, User_massage:{massage}, User_phone: {phone}')
    return render(request, 'catalog/index-contacts.html', )


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


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ['headline', 'content', 'preview', 'creation_date_blog']
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ['headline', 'content', 'preview', 'creation_date_blog']
    success_url = reverse_lazy('catalog:blog_list')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
