from pydantic import BaseModel

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

class CustomerCreate(BaseModel):
    name: str
    email: str

class Customer(BaseModel):
    id: int
    name: str
    email: str
    active: bool = True
