import random

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, PasswordRecoveryForm
from users.models import User
from django.http import HttpResponseRedirect


class RegisterMessageView(TemplateView):
    # model = User
    template_name = 'users_app/register_message.html'


class PasswordRecoveryMessageView(TemplateView):
    template_name = 'users_app/password_recovery_message.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'users_app/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:register_message')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = "".join([str(random.randint(0, 9)) for i in range(10)])
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/register/email_confirm/{token}/'
        send_mail(
            'Подтверждение почты',
            f'Перейдите по ссылке для подтверждения почты {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    # return redirect(reverse('users:login'))
    return HttpResponseRedirect('/users/login/')


class PasswordRecoveryView(CreateView):
    model = User
    template_name = 'users_app/password_recovery_form.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:recovery_message')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = "".join([str(random.randint(0, 9)) for i in range(10)])
        user.token = token
        user.email.unique = False
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/register/email_confirm/{token}/'
        send_mail(
            'Восстановление пароля',
            f'Новый пароль такой-то, перейдите по ссылке {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


def create_new_password(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    # return redirect(reverse('users:login'))
    return HttpResponseRedirect('/users/login/')