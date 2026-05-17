from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Inventory API",
    description="Mini API para gestionar un inventario de productos para el curso de Metodologías de Desarrollo",
    version="1.0.0"
)

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

class Product(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    in_stock: bool = True

products: list[Product] = []
next_id = 1

@app.get("/")
def home():
    return {
        "message": "Bienvenido a Inventory API",
        "docs": "/docs"
    }

@app.get("/products")
def list_products():
    return products

@app.post("/products")
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

    return {
        "message": "Producto creado correctamente",
        "product": new_product
    }

@app.put("/products/{product_id}/out-of-stock")
def mark_out_of_stock(product_id: int):
    for product in products:
        if product.id == product_id:
            product.in_stock = False
            return {
                "message": "Producto marcado como sin stock",
                "product": product
            }

    raise HTTPException(status_code=404, detail="Producto no encontrado")
