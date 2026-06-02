from fastapi import APIRouter, HTTPException
from app.models import ProductCreate
from app.services.product_service import list_products, register_product, set_out_of_stock

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("")
def get_products():
    return list_products()

@router.post("")
def create_product_endpoint(data: ProductCreate):
    product = register_product(data)
    return {
        "message": "Producto creado correctamente",
        "product": product
    }

@router.put("/{product_id}/out-of-stock")
def mark_out_of_stock(product_id: int):
    product = set_out_of_stock(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {
        "message": "Producto marcado como sin stock",
        "product": product
    }
