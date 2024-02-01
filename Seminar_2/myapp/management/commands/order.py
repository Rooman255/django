from myapp.models import Order

def create_order(client, products, total_price):
    order = Order(client=client, total_price=total_price)
    order.save()
    order.products.set(products)
    return order

def get_order(order_id):
    try:
        order = Order.objects.get(id=order_id)
        return order
    except Order.DoesNotExist:
        return None

def update_order(order_id, **kwargs):
    order = get_order(order_id)
    if order:
        for key, value in kwargs.items():
            setattr(order, key, value)
        order.save()
    return order

def delete_order(order_id):
    order = get_order(order_id)
    if order:
        order.delete()
    return order