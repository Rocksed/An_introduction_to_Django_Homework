from django.shortcuts import render

from catalog.forms import ProductForm
from catalog.models import Product


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
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        print(f'User_name: {name}, User_email: {email}, User_massage:{massage}')
    return render(request, 'catalog/cast.html',)
