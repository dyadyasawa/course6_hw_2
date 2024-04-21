from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    template_name = 'users_app/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
