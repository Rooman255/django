from myapp.models import Product

def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product

def get_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product
    except Product.DoesNotExist:
        return None

def update_product(product_id, **kwargs):
    product = get_product(product_id)
    if product:
        for key, value in kwargs.items():
            setattr(product, key, value)
        product.save()
    return product

def delete_product(product_id):
    product = get_product(product_id)
    if product:
        product.delete()
    return product