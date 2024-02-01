
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)
def home_view(request):
    # HTML-вёрстка и данные о вашем первом Django-сайте
    html = "<h1>Добро пожаловать в Магазин!</h1><p>Здесь вы найдете много интересного.</p>"

    # Сохранение данных о посещении страницы в логи
    logger.info("Заходили на страницу магазина")

    return HttpResponse(html)