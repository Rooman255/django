import random

from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
from random import randint, uniform, choices
from datetime import date


class Command(BaseCommand):
    help = 'Заполнение базы данных'

    def handle(self, *args, **options):
        clients = []
        list_name = ['Шишканов Владлен Данилович', 'Непеин Самсон Никифорович', 'Толкачёв Андриян Богданович',
                     'Ковшевникова Галина Фомевна', 'Яблонев Али Романович', 'Ширяева Анна Васильевна',
                     'Будникова Влада Адриановна', 'Белоусов Евграф Саввич', 'Постников Леонид Демьянович',
                     'Логиновский Казимир Валерьевич']
        list_email = ['tradition@gmail.com', 'motheroperation@inbox.ru', 'minute@gmail.com',
                      'productoperation@inbox.ru', 'school@mail.ru', 'operation@inbox.ru', 'coach@gmail.com',
                      'copyschool@mail.ru', 'realityschool@gmail.com', 'recordschool@mail.ru']
        list_city = ['Инза', 'Инкерман', 'Иннополис', 'Инсар', 'Инта', 'Ипатово', 'Ирбит', 'Иркутск', 'Исилькуль',
                     'Искитим', 'Истра', 'Калачинск', 'Калининград', 'Калининск', 'Калтан', 'Калуга', 'Калязин',
                     'Камбарка', 'Каменка', 'Каменногорск', 'Камешково', 'Камызяк', 'Камышин']
        list_phone = [81234567987, 89524654321, 81234567987, 86543223591, 86543223595, 86543223599, 86543823599,
                      83543223599, 89543223545, 85236914726]

        for i in range(5):
            client = Client(name=random.choice(list_name), email=random.choice(list_email),
                            address=random.choice(list_city), phone=random.choice(list_phone))
            client.save()
            clients.append(client)

        products = []
        list_products = ['морковь', 'редис', 'капуста', 'свёкла', 'помидор', 'лук', 'бобы', 'горох', 'огурец', 'укроп',
                         'петрушка', 'репа', 'кабачок', 'тыква', 'перец', 'кочан', 'картофель', 'редька', 'баклажан',
                         'чеснок', 'салат', 'стручок']
        for i in range(10):
            product = Product(name=random.choice(list_products), description='Овощь',
                              price=round(uniform(100, 500), 2), amount=randint(1, 100))
            product.save()
            products.append(product)

        for client in clients:
            for _ in range(20):
                order_products = choices(products, k=3)
                common_price = 0
                for product in order_products:
                    common_price += product.price
                order = Order(client=client, common_price=common_price,
                              date=date(year=2023, month=randint(1, 8), day=randint(1, 26)))
                order.save()
                order.products.set(order_products)
