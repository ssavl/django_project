from django.shortcuts import render
from .forms import AuthForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
import time

class MyLogoutView(LogoutView):
    next_page = '/'


class MyLoginView(LoginView):
    template_name = 'users/login.html'


# def get_name(request):
#     # если это запрос POST, нам нужно обработать данные формы
#     if request.method == 'POST':
#         print(request.method)
#         # создать экземпляр формы и заполнить его данными из запроса:
#         print('у нас POST метод!')
#         form = AuthForm(request.POST)
#         # проверьте, действительно ли это:
#         if form.is_valid():
#             print(request.method)
#             print('у нас форма валидна!')
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Вы успешно вошли в систему!')
#                 AuthForm.add_error('__all__', 'Возникла ошибка, учетная запись не активна!')
#             AuthForm.add_error('__all__', 'Возникла ошибка, Такого пользователя не существует!')
#
#             # редиректим на новый если залогинились URL:
#             return HttpResponseRedirect('')
#
#     # если GET (или любой другой метод) мы создадим пустую форму
#     else:
#         print(request.method)
#
#         print('у нас GET метод! сработал else')
#         form = AuthForm()
#
#     return render(request, 'users/login.html', {'form': form})


