from fastapi import APIRouter
from app.models import ProductCreate
from app.services.product_service import list_products, register_product, set_out_of_stock
from app.utils.validators import validate_exists

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("")
def get_products():
    return list_products()

@router.post("")
def create_product_endpoint(data: ProductCreate):
    return register_product(data)

@router.put("/{product_id}/out-of-stock")
def mark_out_of_stock(product_id: int):
    product = set_out_of_stock(product_id)
    return validate_exists(product, "Producto no encontrado")
