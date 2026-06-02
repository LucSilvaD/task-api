from app.data.product_repository import get_all_products, create_product, mark_product_out_of_stock

def list_products():
    return get_all_products()

def register_product(data):
    return create_product(data)

def set_out_of_stock(product_id):
    return mark_product_out_of_stock(product_id)
