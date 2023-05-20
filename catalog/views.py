from django.shortcuts import render
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
    return render(request, 'catalog/index-contacts.html',)


class BlogListView(generic.ListView):
    model = Blog
# def blog(request):
#     return render(request, 'catalog/blog_list.html',)
