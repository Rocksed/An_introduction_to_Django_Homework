from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, TemplateView

from users.forms import UserForm, UserRegisterForm
from users.models import User


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:product_list')


class ActivationSentView(TemplateView):
    template_name = 'users/activation_sent.html'
