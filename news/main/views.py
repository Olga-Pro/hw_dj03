from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {
        'caption': "Мой сайт"
    }
    return render(request, 'main/index.html', data)


def new(request):
    return render(request, '/main/new.html')


def data(request):
    return HttpResponse("<h1> Новая страница для данных </h1>")


def test(request):
    return HttpResponse("<h1> Новая страница - test </h1>")
