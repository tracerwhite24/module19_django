from django.shortcuts import render
from .forms import UserRegister
from django.contrib.auth.models import User
from .models import Game
from django.core.paginator import Paginator
from .models import News


def menu(request):
    return render(request, 'fourth_task/menu.html')


def store_platform(request):
    return render(request, 'fourth_task/platform.html')


def store_goods(request):
    # Извлекаем все записи из базы данных
    games = Game.objects.all()

    goods = {
        'items': games
    }

    return render(request, 'fourth_task/goods.html', context=goods)


def store_cart(request):
    return render(request, 'fourth_task/cart.html')


def sign_up(request):
    info = {'form_type': 'sign_up'}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Проверяем, существует ли пользователь с таким именем
                if User.objects.filter(username=username).exists():
                    info['error'] = 'Пользователь уже существует'
                else:
                    # Создаём нового пользователя
                    user = User.objects.create_user(username=username, password=password)

                    info['success'] = f'Приветствуем, {username}!'
                    form = UserRegister()  # Сбрасываем форму после успешной регистрации
        else:
            info['error'] = 'Пожалуйста, исправьте ошибки в форме.'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)

    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    return render(request, 'fourth_task/news.html', {'news': news_page})