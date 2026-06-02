from app.models import Product, ProductCreate
products: list[Product] = []
next_id = 1

def get_all_products():
    return products

def create_product(product_data: ProductCreate):
    global next_id
    new_product = Product(
        id=next_id,
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        in_stock=True
    )
    products.append(new_product)
    next_id += 1
    return new_product

def mark_product_out_of_stock(product_id: int):
    for product in products:
        if product.id == product_id:
            product.in_stock = False
            return product
    return None
