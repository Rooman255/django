from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)
def home_view(request):
    # HTML-вёрстка и данные о вашем первом Django-сайте
    html = "<h1>Добро пожаловать!</h1><p>Здесь вы найдете много интересного.</p>"

    # Сохранение данных о посещении страницы в логи
    logger.info("Данные о посещении страницы")

    return HttpResponse(html)


def about_view(request):
    # HTML-вёрстка и данные о вас
    html = "<h1>Обо мне</h1><p>Я - изучаю Django </p>"

    # Сохранение данных о посещении страницы в логи"
    logger.error("Посещение страницы 'О себе'")


    return HttpResponse(html)