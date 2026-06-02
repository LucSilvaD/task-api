from fastapi import FastAPI
from app.routes.product_routes import router

app = FastAPI(
    title="Inventory API",
    description="Mini API para gestionar un inventario de productos para el curso de Metodologías de Desarrollo",
    version="1.0.0"
)
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Bienvenido a Inventory API",
        "docs": "/docs"
    }
