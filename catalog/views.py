from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all()

    }
    return render(request, 'catalog/index.html', context, )

# if request.method == "POST":
# name = request.POST.get('name')
# email = request.POST.get('email')
# massage = request.POST.get('massage')
# print(f'User_name: {name}, User_email: {email}, User_massage:{massage}')
# return render(request, 'catalog/index.html')
